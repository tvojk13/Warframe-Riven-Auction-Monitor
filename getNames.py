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



# while(True):
#
#     session = requests.Session()
#     responce = session.get(main_url).text
#     data = json.loads(responce)
#
#     for auction in data["payload"]["auctions"]:
#
#         if auction["owner"]["status"] == "offline" or auction["owner"]["status"] == "online":
#             continue
#         else:
#             if auction["buyout_price"] <= 300:
#                 price = auction["buyout_price"]
#                 print("====================")
#                 print(price)
#                 contact_with_seller = "/w " + auction["owner"]["ingame_name"] + " hi, i want buy riven for "
#                 print("/w " + auction["owner"]["ingame_name"] + " hi, i want buy riven for ")
#                 #print(auction["owner"]["status"])
#                 notification.notify(message=str(price), app_name='script', title='Rubico riven')
#                 break
#             else:
#                 continue
#
#     session.close()
#     random_sec = random.randint(0, 3)
#     time.sleep(3 + random_sec)

