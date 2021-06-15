import requests
from bs4 import BeautifulSoup

limit = 50
url = f"https://www.indeed.com/jobs?q=python&limit={limit}"

def extract_indeed_pages():
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")

    pagination = soup.find("div",{"class":"pagination"})

    links = pagination.find_all('a')
    spans = []
    for link in links[:-1]:
        spans.append(link.find("span").string)

    max_page = max(spans)
    return max_page

def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{url}&start={page*limit}")
        print(result.status_code)
    