from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job in jobs:
            job_posts = job.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                

            company, region = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_='title')

            job_data = {
                'company': company.string,
                'location': region.string,
                'position': title.string,
            }
            results.append(job_data)
        return results
