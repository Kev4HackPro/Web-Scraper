import requests
from bs4 import BeautifulSoup
import pandas as pd
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
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
    print()

df = pd.DataFrame({'Job Name': job, 'Company Name': company, 'Location': location})
df.to_csv('jobs.csv', index=False, encoding='utf-8')