# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:47:27 2021

@author: Vadim
"""

import json

data = {}
data['participants'] = []
data['participants'].append({
    'name': 'XXX',
    'from': 'Moscow'
})
data['participants'].append({
    'name': 'XXX',
    'from': 'Moscow Region'
})

data['participants'].append({
    'name': 'XXX',
    'from': 'Kazan'
})
print(data)

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)