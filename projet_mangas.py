# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:08:23 2021

@author: lucil
"""

import http.client
conn = http.client.HTTPSConnection("jikan1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "jikan1.p.rapidapi.com",
    'x-rapidapi-key': "20013f0111msh6d05d5288cf7db6p1a1debjsn79fabb5d16d0"
    }

conn.request("GET", "/top/manga/10/manga", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))