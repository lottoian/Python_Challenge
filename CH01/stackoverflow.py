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

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text,"html.parser")
        
        
extract_jobs(get_last_page())