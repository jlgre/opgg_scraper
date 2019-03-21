#!/usr/bin/env python3

import requests
import sys
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
        ranks = soup.find("table", {"class": "champion-index-table tabItems"})
        tbodyclass = "tabItem champion-trend-tier-" + lane
        tbody = ranks.find("tbody", {"class": tbodyclass})

        place, name, win_rate, ban_rate = [],[],[],[]

        for tr in tbody.find_all("tr"):
            raw = tr.find_all("td")
            place.append(raw[0].text.strip())
            name.append(raw[3].find("a").find("div").text.strip())
            win_rate.append(raw[4].text.strip())
            ban_rate.append(raw[5].text.strip())

        return place, name, win_rate, ban_rate


def disp_tier_list(place, name, win_rate, ban_rate, lane):
        """
        Displays data returned from tier lists
        """
        for i in range(0,len(place)):
                if len(name[i]) >= 8:
                        print(place[i] + "\t\t" +  name[i] + "\t" +  win_rate[i] + "\t\t" + ban_rate[i])
                else:
                        print(place[i] + "\t\t" +  name[i] + "\t\t" +  win_rate[i] + "\t\t" + ban_rate[i])


def err():
        """
        Deals with invalid argument input
        """
        print("USAGE:\n\tUse parameter -t to get tier lists \n\tSpecify lane by following with:\n\t\t-t (TOP)\n\t\t-j (JUNGLE) \n\t\t-m (MID)\n\t\t-ad (ADC)\n\t\t-s (SUPPORT)\n\t\t-a (ALL)")


try:

        if sys.argv[1] == "-t" and sys.argv[2] == "-a":

                print("\nTOP TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("TOP")

                disp_tier_list(place, name, win_rate, ban_rate, "TOP")

                print("\nJUNGLE TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("JUNGLE")

                disp_tier_list(place, name, win_rate, ban_rate, "JUNGLE")

                print("\nMID TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("MID")

                disp_tier_list(place, name, win_rate, ban_rate, "MID")

                print("\nADC TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("ADC")

                disp_tier_list(place, name, win_rate, ban_rate, "ADC")

                print("\nSUPPORT TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("SUPPORT")

                disp_tier_list(place, name, win_rate, ban_rate, "SUPPORT")

        elif sys.argv[1] == "-t" and sys.argv[2] == "-t":
                print("\nTOP TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("TOP")

                disp_tier_list(place, name, win_rate, ban_rate, "TOP")

        elif sys.argv[1] == "-t" and sys.argv[2] == "-j":
                print("\nJUNGLE TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("JUNGLE")

                disp_tier_list(place, name, win_rate, ban_rate, "JUNGLE")

        elif sys.argv[1] == "-t" and sys.argv[2] == "-m":
                print("\nMID TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("MID")

                disp_tier_list(place, name, win_rate, ban_rate, "MID")

        elif sys.argv[1] == "-t" and sys.argv[2] == "-ad":
                print("\nADC TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("ADC")

                disp_tier_list(place, name, win_rate, ban_rate, "ADC")

        elif sys.argv[1] == "-t" and sys.argv[2] == "-s":
                print("\nSUPPORT TIER LIST\n")
                print("Tier\t\tName\t\tWin Rate\tBan Rate")
                place, name, win_rate, ban_rate = get_tier_list("SUPPORT")

                disp_tier_list(place, name, win_rate, ban_rate, "SUPPORT")

        else:
            err()


except:
        err()
