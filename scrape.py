import requests
from bs4 import BeautifulSoup

data = requests.get("https://na.op.gg/champion/statistics")

soup = BeautifulSoup(data.text, "html.parser")

ranks = soup.find("table", {"class" : "champion-index-table tabItems"})

print("\nTOP TIER LIST\n")

TOP = ranks.find("tbody", {"class" : "tabItem champion-trend-tier-TOP"})

for tr in TOP.find_all("tr"):
    raw = tr.find_all("td")
    place = raw[0].text.strip()
    name = raw[3].find("a").find("div").text.strip()
    win_rate = raw[4].text.strip()
    ban_rate = raw[5].text.strip()
    print(place, name, win_rate, ban_rate)

print("\nJUNGLE TIER LIST\n")

JUNGLE = ranks.find("tbody", {"class" : "tabItem champion-trend-tier-JUNGLE"})

for tr in JUNGLE.find_all("tr"):
    raw = tr.find_all("td")
    place = raw[0].text.strip()
    name = raw[3].find("a").find("div").text.strip()
    win_rate = raw[4].text.strip()
    ban_rate = raw[5].text.strip()
    print(place, name, win_rate, ban_rate)

print("\nMID TIER LIST\n")

MID = ranks.find("tbody", {"class" : "tabItem champion-trend-tier-MID"})

for tr in MID.find_all("tr"):
    raw = tr.find_all("td")
    place = raw[0].text.strip()
    name = raw[3].find("a").find("div").text.strip()
    win_rate = raw[4].text.strip()
    ban_rate = raw[5].text.strip()
    print(place, name, win_rate, ban_rate)

print("\nADC TIER LIST\n")

ADC = ranks.find("tbody", {"class" : "tabItem champion-trend-tier-ADC"})

for tr in ADC.find_all("tr"):
    raw = tr.find_all("td")
    place = raw[0].text.strip()
    name = raw[3].find("a").find("div").text.strip()
    win_rate = raw[4].text.strip()
    ban_rate = raw[5].text.strip()
    print(place, name, win_rate, ban_rate)

print("\nSUPPORT TIER LIST\n")

SUPPORT = ranks.find("tbody", {"class" : "tabItem champion-trend-tier-SUPPORT"})

for tr in SUPPORT.find_all("tr"):
    raw = tr.find_all("td")
    place = raw[0].text.strip()
    name = raw[3].find("a").find("div").text.strip()
    win_rate = raw[4].text.strip()
    ban_rate = raw[5].text.strip()
    print(place, name, win_rate, ban_rate)