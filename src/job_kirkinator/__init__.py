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

driver.set_page_load_timeout(20)

try:
    print("Opening")
    driver.get("https://jobvision.ir/jobs")
    wait = WebDriverWait(driver, 20)

    job = wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "job-card")
                )
            )

    titles = driver.find_elements(By.CLASS_NAME, "job-card")

    for tag in titles:
        print(tag)
        print(tag.text)

finally:
    driver.quit()
