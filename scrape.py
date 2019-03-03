import requests
from bs4 import BeautifulSoup

data = requests.get('https://na.op.gg/champion/statistics')

soup = BeautifulSoup(data.text, 'html.parser')

ranks = soup.find("table", {"class" : "champion-index-table tabItems"})
rtbody = ranks.find("tbody", {"class" : "tabItem champion-trend-tier-TOP"})

for tr in rtbody.find_all("tr"):
    raw = tr.find_all("td")
    place = raw[0].text.strip()
    name = raw[3].find("a").find("div").text.strip()
    win_rate = raw[4].text.strip()
    ban_rate = raw[5].text.strip()
    print(place, name, win_rate, ban_rate)