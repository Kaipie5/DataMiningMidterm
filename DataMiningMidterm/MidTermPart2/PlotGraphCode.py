#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:18:23 2018

@author: kaim
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

web='https://www.sports-reference.com/olympics/summer/1996/'
req = Request(web)
page = urlopen(req)
soup = BeautifulSoup(page, "lxml")
table = soup.find("div", { "class" : "table_container" })
cells=[]
for row in table.findAll("tr"):
    result = row.findAll("td")
    if len(result) == 6:
        dic = {}
        dic["Rank"] = result[0].get_text()
        dic["Country"] = result[1].get_text()
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
data = data[['Total', 'Rank', 'Country', 'Bronze', 'Silver', 'Gold']]
#print(data)
data['year']=np.repeat(1996,data.shape[0])
data.to_csv(r'format3.csv', header=True, index=None, sep=',', mode='a')

import matplotlib.pyplot as plt

#######PLOT GRAPH################
##Correlation between number of gold medals and rank of Country in Olypmics
numCountries = len(data)
countries = data.head(n=numCountries)['Gold']
numGolds = []
for i in range(0, numCountries):
    numGolds.append(int(countries[i]))
countries = data.head(n=numCountries)['Rank']
numRank = []
for i in range(0, numCountries):
    numRank.append(int(countries[i]))
plt.plot(numRank, numGolds)
plt.title("Country Rank Compared to Number of Gold Medals")
plt.xlabel("Country Rank")
plt.ylabel("Number of Gold Medals")
