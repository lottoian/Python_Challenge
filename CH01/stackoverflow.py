import requests
from bs4 import BeautifulSoup

i = 1
URL = f"https://stackoverflow.com/jobs?q=python"

def get_last_page():

    result = requests.get(URL)

    soup = BeautifulSoup(result.text,"html.parser")

    pages = soup.find("div",{"class":"s-pagination"}).find_all('a')
    last_page = pages[:-1]
    return int(last_page[-1].get_text(strip=True))

def extract_job(html):
    title = html.find("h2",{"class":"mb4"}).find('a')["title"]
    company, location = html.find("h3",{"class":"fc-black-700"}).find_all("span",recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    
    '''
    company = html.find("h3",{"class":"fc-black-700"}).find("span").string
    if company is None:
        company = "Unknown"
    location = html.find("span",{"class":"fc-black-500"}).string
    print(company)
    '''
    
    return {"title":title,"company":company,"location":location,"apply_link":f"https://stackoverflow.com/jobs/{job_id}"}



def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Export page StackOver {page}")
        result = requests.get(f"{URL}&pg={0+1}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    print("---------------------------------")

    return jobs
        
extract_jobs(get_last_page())