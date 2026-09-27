from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.binary_location = "/usr/sbin/brave"
options.page_load_strategy = "none"
options.add_argument("--headless=new")

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
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card")))

    jobs = driver.find_elements(By.CLASS_NAME, "job-card")

    for job in jobs:
        html = job.get_attribute("outerHTML")
        print(html)
        print(job.tag_name)
        print(job.text)
        links = job.find_elements(By.TAG_NAME, "a")

finally:
    driver.quit()
