#! python3

import sys
import os

import scrape_tools.reddit_community_scraper as scraper


with open(r'C:\315\crawl\subs_to_collect.txt') as subs:
    subs_to_collect = [l.strip() for l in subs]

for sub in subs_to_collect:
    outfile = sub+"_postdata_"+"-"+".json"
    scraper.scraper(sub, outfile, True, True) # First boolean param is for collecting posts, second boolean param is for collecting comments
