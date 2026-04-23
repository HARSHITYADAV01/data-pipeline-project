import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for page in range(0, 2):
    url = f"https://www.indeed.com/jobs?q=data+engineer&start={page*10}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('div', class_='job_seen_beacon')

    for job in jobs:
        title = job.find('h2')
        company = job.find('span', class_='companyName')
        location = job.find('div', class_='companyLocation')

        data.append({
            "title": title.text.strip() if title else None,
            "company": company.text.strip() if company else None,
            "location": location.text.strip() if location else None
        })

df = pd.DataFrame(data)
df.dropna(subset=["company"], inplace=True)
df.drop_duplicates(inplace=True)

df.to_csv("jobs.csv", index=False)

print("Pipeline done!")
