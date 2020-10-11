#!/usr/bin/env python
# coding: utf-8

# # Downloading Files from the Web with the requests Module, and saving Downloaded Files to the Hard Drive

# Following guidance from the very resourceful website automatetheboringstuff.com, I learned how to use the Requests module to download the daily data files from the coronavirus.data.gov.uk site by writing the files ('wb'). Helpfully, links are provided directly on the site to download the data, and I was easily able to copy the address of the CSV files I wanted to download to paste into my code - it feels too easy!
# 
# In lots of circumstances you need to dig deeper to scrape data, and automatetheboringstuff.com has useful examples of how to pick apart websites by accessing a web broswer's developer tools and inspecting the HTML. This may be useful to me for future projects, or for any data I require in the future within my Covid dashboard project that I cannot directly download using a link. 
# 
# I feel I've barely even scratched the surface of utilising the requests module, and hope to use it more in future, maybe even just to have a play around with how I can harness requests to automate some routine stuff. However, for the purposes of my current project to create several dashboards/reports of Covid data, this would take me on too much of a tangent. I'll just have to dip my toes for now, and pencil this down for a future project.
# 
# The code below takes each CSV file and saves it into my Python directory. The code was written using Spyder - my new preferred development environment for writing Python scripts:

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:00:16 2020

@author: elsie
"""


import requests
res = requests.get('https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation&structure=%7B%22areaType%22:%22areaType%22,%22areaName%22:%22areaName%22,%22areaCode%22:%22areaCode%22,%22date%22:%22date%22,%22newCasesBySpecimenDate%22:%22newCasesBySpecimenDate%22,%22cumCasesBySpecimenDate%22:%22cumCasesBySpecimenDate%22%7D&format=csv')
res.raise_for_status()
playFile = open('Cases_by_specimen_date.csv', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)
        
res = requests.get('https://api.coronavirus.data.gov.uk/v1/data?filters=areaName=United%2520Kingdom;areaType=overview&structure=%7B%22areaType%22:%22areaType%22,%22areaName%22:%22areaName%22,%22areaCode%22:%22areaCode%22,%22date%22:%22date%22,%22newCasesByPublishDate%22:%22newCasesByPublishDate%22,%22cumCasesByPublishDate%22:%22cumCasesByPublishDate%22%7D&format=csv')
res.raise_for_status()
playFile = open('Cases_by_date_reported.csv', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)
        
res = requests.get('https://coronavirus.data.gov.uk/downloads/msoa_data/MSOAs_latest.csv')
res.raise_for_status()
playFile = open('Cases_by_area_England.csv', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)
        
res = requests.get('https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation&structure=%7B%22areaType%22:%22areaType%22,%22areaName%22:%22areaName%22,%22areaCode%22:%22areaCode%22,%22date%22:%22date%22,%22newDeaths28DaysByPublishDate%22:%22newDeaths28DaysByPublishDate%22,%22cumDeaths28DaysByPublishDate%22:%22cumDeaths28DaysByPublishDate%22%7D&format=csv')
res.raise_for_status()
playFile = open('Deaths_by_date.csv', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)        
        

