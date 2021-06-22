import requests
from bs4 import BeautifulSoup

limit = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={limit}"

def get_last_page():
    
    result = requests.get(URL)

    soup = BeautifulSoup(result.text,"html.parser")

    pagination = soup.find("div",{"class":"pagination"})

    links = pagination.find_all("a")
    print(len(links))
    pages =[]

    for link in links[:-1]:
        pages.append(int(link.find("span").string))

    max_page = max(pages)
    return max_page


def extract_job(html):
    title = html.find("h2",{"class":"title"}).find('a')["title"]
    company = html.find("span",{"class":"company"})
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    '''
    if company is not None:
        company_anchor = company.find('a')
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
        company = company.strip()
    else:
        company = "Unkown"
   
    '''
    if company is None:
        company = "Unknown"
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    
    return {'title':title,'company':company,'location':location,"link":f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}"}

def extract_jobs(last_page):
    jobs = []
    for x in range(last_page):
        print(f"Export Page {x}")
        result = requests.get(f"{URL}&start={0*limit}")
        print(f"Status {result.status_code}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            print(job)
    print("---------------------------------")
            
def get_jobs():

    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs