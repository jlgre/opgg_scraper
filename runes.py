#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This code is given to the public domain

import requests
from bs4 import BeautifulSoup

def get(lane, name):
    """
    Gets the runes of specific champion and lane
    """
    rune_options = []
    data = requests.get("https://na.op.gg/champion/" +
                        name + "/statistics/" + lane)
    soup = BeautifulSoup(data.text, "html.parser")
    paths = soup.find_all('div', class_ = "champion-stats-summary-rune__name")
    rune_paths = ([path.text.split(' + ') for path in paths])
    active_runes = soup.find_all('div', class_ = ["perk-page__item perk-page__item--active",\
                                                  "perk-page__item perk-page__item--keystone perk-page__item--active"])
    # Determine the Primary/Secondary runes
    all_runes = []
    for runes in active_runes:
        all_runes.append(runes.find('img', alt=True)['alt'])

    # Determine the shards for each build
    all_shards = []
    active_shards = soup.find_all('div', class_ = "fragment__detail")
    for i in range(len(active_shards)):
        shard_option = active_shards[i].find_all('div', class_ = "fragment__row")
        _shard = []
        for j in range(len(shard_option)):
            for k in range(3):
                if ('class="active tip"' in str(shard_option[j].find_all('img')[k])):
                    _shard.append(k)

    # TODO: clean up data processing. op.gg seems always have 4 options but that could change
    # Formats data into a list of all runes
        if i in [0,1]:
            primary_path = [rune_paths[0][0],all_runes[(6*i):(4+(i*6))]]
            secondary_path = [rune_paths[0][1],all_runes[4+(6*i):(6+(i*6))]]
            rune_options.append([primary_path,secondary_path,_shard])
        else:
            primary_path = [rune_paths[1][0],all_runes[(6*i):(4+(i*6))]]
            secondary_path = [rune_paths[1][1],all_runes[4+(6*i):(6+(i*6))]]
            rune_options.append([primary_path,secondary_path,_shard])
    return(rune_options)



def display(rune_options):
    """
    Displays runes of a specific champion and lane
    """
    shard_rows = ['Offense Adaptive Force +9','Offense +10% Attack Speed','Offense +1-10% CDR (based on level)'],\
                 ['Offense Adaptive Force +9','Flex +6 Armor','Flex +8 Magic Resist'],\
                 ['Defense +15-90 Health (based on level)','Flex +6 Armor','Flex +8 Magic Resist']
    for rune_set in rune_options:
        print(f"Primary Runes \n{rune_set[0][0]}")
        for runes in rune_set[0][1]:
            print(runes)
        print(f"\nSecondary Runes \n{rune_set[1][0]}")
        for runes in rune_set[1][1]:
            print(runes)
        print("\nShards")
        for shard in range(len(rune_set[2])):
            print(shard_rows[shard][rune_set[2][shard]])
        print("===========")
