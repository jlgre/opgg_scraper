import requests
from bs4 import BeautifulSoup

def get(lane):
    """
    gets a tier list from a specified lane
    lane options:
            "TOP"
            "JUNGLE"
            "MID"
            "ADC"
            "SUPPORT"
    """
    lane = lane.upper()
    data = requests.get("https://na.op.gg/champion/statistics")
    soup = BeautifulSoup(data.text, "html.parser")
    ranks = soup.find("table", {"class": "champion-index-table tabItems"})
    tbodyclass = "tabItem champion-trend-tier-" + lane
    tbody = ranks.find("tbody", {"class": tbodyclass})

    place, name, win_rate, ban_rate = [],[],[],[]

    for tr in tbody.find_all("tr"):
        raw = tr.find_all("td")
        data = {}
        place.append(raw[0].text.strip())
        name.append(raw[3].find("a").find("div").text.strip())
        win_rate.append(raw[4].text.strip())
        ban_rate.append(raw[5].text.strip())

    return place, name, win_rate, ban_rate


def display_header(lane):
    """
    Displays table headers and lables for tier lists
    """
    if (lane == "all"):
        for i in ["top", "jungle", "mid", "adc", "support"]:
            display_header(i)
    else:
        print("\n"+ lane.upper() + " TIER LIST\n\nTier\t\tName\t\tWin Rate\tBan Rate")


def display(place, name, win_rate, ban_rate, lane):
    """
    Displays data returned from tier lists
    """
    display_header(lane)
    for i in range(0,len(place)):
            if len(name[i]) >= 8:
                    print(place[i] + "\t\t" +  name[i] + "\t" +  win_rate[i] + "\t\t" + ban_rate[i])
            else:
                    print(place[i] + "\t\t" +  name[i] + "\t\t" +  win_rate[i] + "\t\t" + ban_rate[i])





