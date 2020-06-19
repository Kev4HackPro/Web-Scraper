import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
table_data = soup.find('table', class_='table table-striped table-bordered table-hover table-condensed table-list')
headers = []
for title in table_data.find_all('th'):
    title = title.text
    headers.append(title)

df = pd.DataFrame(columns = headers)
for row in table_data.find_all('tr')[1:]:
    row_data = row.find_all('td')
    row = [tr.text for tr in row_data] 
    length = len(df)
    df.loc[length] = row

df.to_csv('stat.csv', index=False, encoding='utf-8')