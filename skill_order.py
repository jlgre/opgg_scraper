import requests
from bs4 import BeautifulSoup


def get(lane, name):
    """
    Gets skill order of specific champion and lane
    """
    data = requests.get("https://na.op.gg/champion/" +
                        name + "/statistics/" + lane)
    soup = BeautifulSoup(data.text, "html.parser")
    skills = soup.find("table", {"class": "champion-skill-build__table"})
    tbody = skills.find("tbody")
    tr = tbody.find_all("tr")[1]
    skill_table = []
    for td in tr.find_all("td"):
        if td.text.strip() == 'Q' or td.text.strip() == 'W' or td.text.strip() == 'R' or td.text.strip() == 'E':
            skill_table.append(td.text.strip())

    return skill_table


def display(skills):
    """
    Displays skill order of a specific champion and lane
    """
    outstring = ""
    for i in skills:
        outstring = outstring + i + "->"
    print(outstring[:-2])
