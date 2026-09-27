import requests
from bs4 import BeautifulSoup

def main():
    print("fetching")
    req = requests.get("https://jobvision.ir/jobs")
    soup = BeautifulSoup(req.text, "html.parser")
    jobs = soup.find_all("div", class_="job-card")
    print(jobs)
    for job in jobs:
        print(job.prettify())

if __name__ == "__main__":
    main()
