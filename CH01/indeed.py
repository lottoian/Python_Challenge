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
    #for page in range(last_page):
    result = requests.get(f"{url}&start={0*limit}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"job_seen_beacon"})
      
    for text in results:
        title = text.find("h2",{"class":"jobTitle jobTitle-color-purple"}).find("span")["title"]
        if title is not None:
            print(title)
        
max_indeed_pages = extract_indeed_pages()
print(max_indeed_pages)
extract_indeed_jobs(int(max_indeed_pages))
