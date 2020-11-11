#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import json

server_slug = "Gehennas"
with open(server_slug + "_alliance.json") as file:
    alliance_json = json.load(file)
with open(server_slug + "_horde.json") as file:
    horde_json = json.load(file)
files = [alliance_json, horde_json]
pd_files = [pd.json_normalize(data=f, meta="slug", record_path='data') for f in files]
prices = pd.merge(pd_files[0], pd_files[1], on=['itemId'], suffixes=["_a", "_h"])
with open('./item_data.json') as f:
    json_items = json.load(f)
    f.close()
items = pd.json_normalize(json_items)
items = items[['itemId', 'name']]
prices = pd.merge(prices, items, on="itemId")
