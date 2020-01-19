# OPGG Scraper

This is a simple python scraper to pull down data from [opgg](https://op.gg).

Currently supports tier list for all lanes as well as skill orders for a specified champion in a specified lane.

This is also based on very specific formatting of opgg's website, so a redesign by them could break this at any time.

## Usage
|Command|Modifiers|Description|
|-|-|-|
|-t|all|Display tier list of all lanes|
||adc|Display adc tier list|
||jungle|Display jungle tier list|
||support|Display mid tier list|
||support|Display support tier  list|
||top|Diplay top lane tier list|
|-so|{name} {lane}|Display skill orders for a given champion and lane|

## Current TODOs:
* get data for best runes

## Working TODOs:
* get data for best builds

## Things I have learned
* Examining HTML structure for relevant data
* Use Beautiful Soup to make scraping easier
