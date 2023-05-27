import requests
import json

def get_names():
    """load weapon names from json file. if it does not exit, it will be created"""
    try:
        weapon_names = json.load(open("weapon_names.json", 'r'))
    except:

        items_url = "https://api.warframe.market/v1/riven/items"

        session = requests.Session()
        items_responce = session.get(items_url).text
        items_data = json.loads(items_responce)
        session.close()

        weapons = []

        for weapon in items_data["payload"]["items"]:
            weapons.append(weapon["url_name"])

        weapons.sort()

        json.dump(weapons, open("weapon_names.json", 'w'))

    return weapon_names


