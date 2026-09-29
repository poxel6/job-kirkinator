from collections import Counter

from selenium.webdriver.chrome.webdriver import WebDriver

from job_kirkinator.models import Job
from job_kirkinator.pages import JobDetailPage, JobPage


class Scraper:
    pass


class JobVisionScraper(Scraper):
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.job_page: JobPage = JobPage(driver)
        self.details_page: JobDetailPage = JobDetailPage(driver)
        self.jobs: list[Job] = []
        self.keywords: Counter[str] = Counter()
        self.save_delay: int = 0
        self.page: int = 0

    def scrape_jobs(self, page: int = 1) -> list[Job]:
        self.job_page.open(page)

        urls = self.job_page.get_job_urls()
        jobs: list[Job] = []

        for url in urls:
            job = Job.job_from_url(url)
            print(f"Created job with id {job.id}")
            jobs.append(job)
        self.jobs = jobs
        return jobs

    def scrape_details(self) -> Counter[str]:
        jobs = self.jobs or self.scrape_jobs()
        for job in jobs:
            print(f"Searching details of {job.title}")
            self.details_page.open(job.id)

            links = self.details_page.get_links()
            for link in links:
                job = Job.job_from_url(link)

                if any(existing.id == job.id for existing in jobs):
                    continue

                print(f"Created job with id {job.id}")
                jobs.append(job)

            keywords = self.details_page.get_keywords()
            self.keywords += keywords
            self.jobs = jobs

            self.save_delay += 1
            if self.save_delay >= 10:
                print("Autosaving... ")
                self.save_state()
                self.save_delay = 0

        if self.page > 5:
            print("Reached max page limit, returning...")
            return self.keywords
        else:
            print("Scraping next page...")
            self.page += 1
            jobs = self.scrape_jobs(self.page)
            for job in jobs:
                if any(existing.id == job.id for existing in jobs):
                    continue

                print(f"Created job with id {job.id}")
                jobs.append(job)
            self.jobs = jobs
            return self.scrape_details()

    def save_state(self):
        print("writing keywords to file")
        with open("keywords.csv", "w", encoding="utf-8") as f:
            _ = f.write(f"keyword, count\n")
            for keyword, count in self.keywords.most_common():
                _ = f.write(f"{keyword}, {count}\n")
