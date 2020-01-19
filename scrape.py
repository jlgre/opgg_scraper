#!/usr/bin/env python3
import sys

import requests

import skill_order
import tier_list


def help_message():
    """
    Deals with invalid argument input
    """
    print(
        "USAGE:\n\t\"-t {lane}\" or \"-t all\" to get tier list\n\t\"-so {champion} {lane}\" to get skill order")


def main():
    try:
        if sys.argv[1] == "-t" and sys.argv[2] in ["top", "TOP", "adc", "ADC", "mid", "MID", "jungle", "JUNGLE", "all", "ALL", "support", "SUPPORT"]:
            lane = sys.argv[2]
            if lane == "all" or "ALL" or "All":
                for indv in ["top", "jungle", "mid", "adc", "support"]:
                    place, name, win_rate, ban_rate = tier_list.get(indv)
                    tier_list.display(place, name, win_rate, ban_rate, indv)
            else:
                place, name, win_rate, ban_rate = tier_list.get(lane)
                tier_list.display(place, name, win_rate, ban_rate, lane)
        elif sys.argv[1] == "-so":
            skills = skill_order.get(sys.argv[3], sys.argv[2])
            skill_order.display(skills)
        else:
            help_message()

    except requests.exceptions.ConnectionError:
        print("\nCONNECTION ERROR - check connection and try again")


if __name__ == "__main__":
    main()
