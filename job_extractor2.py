import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import pandas as pd
from contextlib import closing


def simple_get(url):
    try:
        with closing(requests.get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error(f"Error during requests {url} {str(e)}")
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


url = 'https://www.monster.com/jobs/search/?q=Data-Science&where=USA'
page = requests.get(url)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job = []
company = []
location = []
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    job.append(title_elem.text.strip())
    company.append(company_elem.text.strip())
    location.append(location_elem.text.strip())

df = pd.DataFrame({'Job Name': job, 'Company Name': company, 'Location': location})
df.to_csv('jobs_.csv', index=False, encoding='utf-8')