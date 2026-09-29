import csv
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from job_kirkinator.scraper import JobVisionScraper


def get_driver():
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/sbin/chromium"
    options.page_load_strategy = "eager"
    # options.add_argument("--headless=new")

    service = Service("/usr/bin/chromedriver")

    return webdriver.Chrome(
        service=service,
        options=options,
    )


def main():
    driver = get_driver()
    scraper = JobVisionScraper(driver)
    try:
        _ = scraper.scrape_jobs()
        _ = scraper.scrape_details()

    except KeyboardInterrupt:
        print("stopping")

    finally:
        scraper.save_state()
        driver.quit()

if __name__ == "__main__":
    main()
