import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://remoteok.com/remote-dev-jobs"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

for job in soup.find_all("tr", class_="job"):
    
    title = job.find("h2")
    company = job.find("h3")

    if title and company:
        jobs.append({
            "Job Title": title.text.strip(),
            "Company": company.text.strip()
        })

df = pd.DataFrame(jobs)

keywords = ["html", "javascript", "technical support"]

filtered_jobs = df[df["Job Title"].str.lower().str.contains("|".join(keywords))]

print(filtered_jobs)

filtered_jobs.to_csv("jobs.csv", index=False)
