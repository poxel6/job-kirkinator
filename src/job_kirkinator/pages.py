from collections import Counter
from typing import final

from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    pass


@final
class JobPage(Page):
    URL = "https://jobvision.ir/jobs/category/developer"
    JOB_CARD_SELECTOR = "a.mobile-job-card"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 100)

    def open(self, page: int = 1):
        url = f"{self.URL}?page={page}&sort=1"
        print(f"Opening {url} in browser.")
        self.driver.get(url)

    def get_job_cards(self):
        print("Waiting for job...")
        return self.wait.until(
            lambda driver: (
                driver.find_elements(By.CSS_SELECTOR, self.JOB_CARD_SELECTOR) or False
            )
        )

    def get_job_urls(self) -> list[str]:
        cards = self.get_job_cards()
        return [url for card in cards if (url := card.get_attribute("href"))]


@final
class JobDetailPage(Page):
    URL = "https://jobvision.ir/jobs"
    JOB_DETAIL_SELECTOR = (
        "div.jvt-flex.jvt-flex-wrap.jvt-gap-x-3 > app-tag > span.tag > span.tag-title"
    )
    JOB_CARD_LINK_SELECTOR = 'section.job-card a[href^="/jobs/"]'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 100)

    def open(self, id: int):
        url = f"{self.URL}/{id}"
        self.driver.get(url)

    def get_keywords(self) -> Counter[str]:
        print("Waiting for job details...")

        safe_mode = True
        if safe_mode:
            try:
                self.wait.until(
                    lambda driver: driver.execute_script(
                        "return document.readyState === 'complete'"
                    )
                )

            except TimeoutException:
                pass
        else:
            _ = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

        keywords = self.driver.execute_script(
            """
            return Array.from(
                document.querySelectorAll(arguments[0])
            )
            .map(element => element.textContent.trim())
            .filter(Boolean);
            """,
            self.JOB_DETAIL_SELECTOR,
        )

        print(f"Found {len(keywords)} keywords")
        return Counter(keywords)

    def get_links(self) -> list[str]:
        links = self.driver.find_elements(By.CSS_SELECTOR, self.JOB_CARD_LINK_SELECTOR)
        all_links = []
        for link in links:
            if link:
                all_links.append(link.get_attribute("href"))

        return all_links

    def get_descriptions(self):
        pass
