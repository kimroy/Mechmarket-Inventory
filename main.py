from dotenv import load_dotenv
import os
import requests
import datetime
import numpy as np
import pandas as pd

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

response = requests.get("https://oauth.reddit.com/r/mechmarket/new", headers=headers, params={"limit" : "3"})
posts = []

for post in response.json()["data"]["children"]:
    posts.append([
        post["data"]["name"], 
        post["data"]["title"], 
        post["data"]["author"], 
        datetime.date.fromtimestamp(post["data"]["created"]), 
        ("https://reddit.com/r/mechmarket/comments/" + post["data"]["permalink"]), 
        post["data"]["selftext"]
    ])

df = pd.DataFrame(posts, columns=["post_id", "title", "author", "date", "link", "text"])

# to:do
# Frequnecy of sales/listings of a certain product using panda
# Valid Locations
#   [United States]: US [Canada]: CA [Australia]: AU [European Union]: EU [United Kingdom]: UK