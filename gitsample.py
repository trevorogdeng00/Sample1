import requests

GITHUB_USERNAME = "trevorogdeng00"
response = requests.get(f"https://api.github.com/users/{GITHUB_USERNAME}/repos")

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(repo["name"], "➡️", repo["html_url"])
else:
    print("Error:", response.status_code)
