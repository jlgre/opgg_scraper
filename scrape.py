import requests
from bs4 import BeautifulSoup

def get_tier_list(lane):
	"""
	gets a tier list from a specified lane
	lane options:
		"TOP"
		"JUNGLE"
		"MID"
		"ADC"
		"SUPPORT"
	"""
	data = requests.get("https://na.op.gg/champion/statistics")
	soup = BeautifulSoup(data.text, "html.parser")
	ranks = soup.find("table", {"class" : "champion-index-table tabItems"})
	tbodyc = "tabItem champion-trend-tier-" + lane
	tbody = ranks.find("tbody", {"class" : tbodyc})

	place, name, win_rate, ban_rate = [],[],[],[]

	for tr in tbody.find_all("tr"):
	    raw = tr.find_all("td")
	    place.append(raw[0].text.strip())
	    name.append(raw[3].find("a").find("div").text.strip())
	    win_rate.append(raw[4].text.strip())
	    ban_rate.append(raw[5].text.strip())

	return place, name, win_rate, ban_rate



print("\nTOP TIER LIST\n")
place, name, win_rate, ban_rate = get_tier_list("TOP")

for i in range(0,len(place)):
	print(place[i], name[i], win_rate[i], ban_rate[i])

print("\nJUNGLE TIER LIST\n")
place, name, win_rate, ban_rate = get_tier_list("JUNGLE")

for i in range(0,len(place)):
	print(place[i], name[i], win_rate[i], ban_rate[i])

print("\nMID TIER LIST\n")
place, name, win_rate, ban_rate = get_tier_list("MID")

for i in range(0,len(place)):
	print(place[i], name[i], win_rate[i], ban_rate[i])

print("\nADC TIER LIST\n")
place, name, win_rate, ban_rate = get_tier_list("ADC")

for i in range(0,len(place)):
	print(place[i], name[i], win_rate[i], ban_rate[i])

print("\nSUPPORT TIER LIST\n")
place, name, win_rate, ban_rate = get_tier_list("SUPPORT")

for i in range(0,len(place)):
	print(place[i], name[i], win_rate[i], ban_rate[i])