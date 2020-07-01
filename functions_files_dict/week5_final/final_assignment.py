#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:36:13 2020

@author: leichen
"""
import matplotlib.pyplot as plt
x = []
y = []
i = 0
debug = True

with open('/Users/leichen/Documents/coursera/python3_programming/functions_files_dict/week5_final/resulting_data.csv') as fd:
    for line in fd:
        if i == 0:
            i += 1
            continue
        line = line.split(',')
        net_score = int(line[-1])
        retweets = int(line[0])
        x.append(net_score)
        y.append(retweets)
        i += 1
if debug:
    print(x)
    print(y)
    
plt.figure(figsize=(12,12), dpi=80)
    
plt.scatter(x, y, marker='o')
plt.xlabel('Net Score')
plt.ylabel('Number of Retweets')
plt.title('Sample Sentiment Analysis Result')
