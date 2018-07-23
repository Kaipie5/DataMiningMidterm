#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:18:23 2018

@author: kaim
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

web='https://www.sports-reference.com/olympics/summer/2016/'
req = Request(web)
page = urlopen(req)
soup = BeautifulSoup(page, "lxml")
table = soup.find("table", { "id" : "athletes" })
cells=[]
for row in table.findAll("tr"):
    result = row.findAll("td")
    if len(result) == 6:
        dic = {}
        dic["Rank"] = result[0].get_text()
        dic["Athlete"] = result[1].get_text()
        dic["Gold"] = result[2].get_text()
        dic["Silver"] = result[3].get_text()
        dic["Bronze"] = result[4].get_text()
        dic["Total"] = result[5].get_text()
        cells.append(dic)
import pandas as pd
import numpy as np
data=pd.DataFrame(cells)
#data = data[['Rank', 'Country', 'Bronze', 'Silver', 'Gold', 'Total']]
#data = data[['Country', 'Rank', 'Bronze', 'Silver', 'Gold', 'Total']]
data = data[['Total', 'Rank', 'Athlete', 'Bronze', 'Silver', 'Gold']]
#print(data)
data['year']=np.repeat(2016,data.shape[0])
data.to_csv(r'format3.csv', header=True, index=None, sep=',', mode='a')

import matplotlib.pyplot as plt

#
############PIE CHART#################
##Distribution of the Number of Gold Medals earned by the top ten Athletes
numCountries = 10
labels = data.head(n=numCountries)['Athlete']
countries = data.head(n=numCountries)['Gold']
explode =[]
countryTotals = []
for i in range(0, numCountries):
    countryTotals.append(int(countries[i]))
    explode.append(0)
    
countryLabels = {}
for i in range(0, numCountries):
    countryLabels[i] = (labels[i])

plt.pie(countryTotals, explode, countryLabels.values())
plt.title("Total Gold Medals For Top Ten Athletes")
