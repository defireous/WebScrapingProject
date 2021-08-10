import requests
from bs4 import BeautifulSoup
import pandas as pd


def getUrl(url):
    response = requests.get(url).text
    return response


response = getUrl('https://pythonjobs.github.io/')
soup = BeautifulSoup(response, 'lxml')

jobs = soup.find_all('div', class_='job')

name_list = []
workplace_list = []
calendar_list = []
type_list = []
office_list = []
more_info_list = []
job_description_list = []

for job in jobs:
    job_detail = job.find_all('span', class_='info')
    temp_list = []
    for i in job_detail:
        temp_list.append(i.text)

    name_list.append(job.h1.a.text)
    workplace_list.append(temp_list[0])
    calendar_list.append(temp_list[1])
    type_list.append(temp_list[2])
    office_list.append(temp_list[3])
    more_info_list.append(job.a['href'])
    job_description_list.append(job.p.text)

job_frame = {'Position': name_list, 'Workplace': workplace_list, 'Calendar': calendar_list,
             'Type': type_list, 'Office': office_list, 'Description': job_description_list, 'More Info': ['https://pythonjobs.github.io/' + i[1:] for i in more_info_list]}

job_dt = pd.DataFrame(job_frame)
out_file = job_dt.to_csv('PythonJobs.csv', index=False)
