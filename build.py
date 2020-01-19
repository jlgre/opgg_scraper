import requests
from bs4 import BeautifulSoup


def get(lane, name):
    """
    Gets build for a champion in a specific lane
    """
    build = {
        'starter_items1': [],
        'starter_items2': [],
        'build1': [],
        'build2': [],
        'build3': [],
        'boot1': [],
        'boot2': []
    }
    data = requests.get("https://na.op.gg/champion/" +
                        name + "/statistics/" + lane)
    soup = BeautifulSoup(data.text, "html.parser")
    table = soup.find_all("table", {"class": "champion-overview__table"})
    tbody = table[1].find("tbody")
    tr = tbody.find("tr", {"class": "champion-overview__row"})
    td = tr.find("td", {"class": "champion-overview__data"})
    ul = td.find("ul", {"class": "champion-stats__list"})
    li = ul.find_all("li")
    for i in li:
        try:
            mystr = i['title']
            start = mystr.find('>') + 1
            end = mystr.find('<', 1)
            build['starter_items1'].append(mystr[start:end])
        except KeyError:
            pass
    print(build)


if __name__ == '__main__':
    get('middle', 'annie')
