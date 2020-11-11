#!/usr/bin/env python3

import requests
import json
server_slug = "Gehennas"
endpoint = "https://api.nexushub.co/wow-classic/v1/items/"
alliance_req = requests.get(endpoint + server_slug + "-alliance")
horde_req = requests.get(endpoint + server_slug + "-horde")
with open(server_slug+"_horde.json", 'w') as file:
    json.dump(horde_req.json(), file)
with open(server_slug+"_alliance.json", 'w') as file:
    json.dump(alliance_req.json(), file)
