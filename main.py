from dotenv import load_dotenv
import os
import requests

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

login_info = {
    'grant_type': 'password',
    'username': USERNAME,
    'password': PASSWORD
}

headers = {"User-Agent": "MarketTracker/0.0.1"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=login_info, headers=headers)

TOKEN = response.json()["access_token"]
headers["Authorization"] = f"bearer {TOKEN}"

response = requests.get("https://oauth.reddit.com/r/mechmarket/new", headers=headers, params={"limit" : "1"})

for post in response.json()["data"]["children"]:
    print(post["data"]["title"])
    print(post["data"]["author"])
    print(post["data"]["created"])
    print("https://reddit.com" + post["data"]["permalink"])

# print(response.json())
# Frequnecy of sales/listings of a certain product using panda