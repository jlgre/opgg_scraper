import requests
from bs4 import BeautifulSoup


def get(lane, name):
    """
    Gets build for a champion in a specific lane
    """
    build = [
        ('starter_items_1', []),
        ('starter_items_2', []),
        ('build_1', []),
        ('build_2', []),
        ('build_3', []),
        ('build_4', []),
        ('build_5', []),
        ('boot_1', []),
        ('boot_2', []),
        ('boot_3', [])
    ]
    data = requests.get("https://na.op.gg/champion/" +
                        name + "/statistics/" + lane)
    soup = BeautifulSoup(data.text, "html.parser")
    table = soup.find_all("table", {"class": "champion-overview__table"})
    tbody = table[1].find("tbody")
    tr = tbody.find_all("tr", {"class": "champion-overview__row"})
    for i in range(0, 10):
        td = tr[i].find("td", {"class": "champion-overview__data"})
        ul = td.find("ul", {"class": "champion-stats__list"})
        li = ul.find_all("li")
        for j in li:
            try:
                mystr = j['title']
                start = mystr.find('>') + 1
                end = mystr.find('<', 1)
                build[i][1].append(mystr[start:end])
            except KeyError:
                pass
    return build


def display(data):
    for i in data:
        build_items = ''
        for j in i[1]:
            build_items += j
            build_items += ', '
        print(i[0], ': ', build_items[:len(build_items) - 2])
