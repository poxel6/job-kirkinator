from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.binary_location = "/usr/sbin/brave"
options.page_load_strategy = "eager"
# options.add_argument("--headless=new")

service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(
    service=service,
    options=options,
)

try:
    print("Opening")
    driver.get(url="https://jobvision.ir/jobs")
    print("retirived content")

    wait = WebDriverWait(driver, 100)

    print("searching for jobs")
    jobs = wait.until(
        lambda driver: (
            driver.find_elements(By.CSS_SELECTOR, "a.mobile-job-card") or False
        )
    )

    print("jobs:", len(jobs))

    for job in jobs:
        print(job.get_attribute("outerHTML"))

finally:
    driver.quit()
