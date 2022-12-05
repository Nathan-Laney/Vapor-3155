import requests
from models import db
from datetime import date
from src.repositories.game_repository import game_repository_singleton
from app import app

# Gets authorization to use IGDB
client_id = 'nnmpkjm8cks3623ypg6d9j68f3b8rq'
client_secret = 'w01q5virehfbuoaguo9lvuduhts7dj'

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body)

# Outputs the given access token 
keys = r.json()

print(keys)


# Gens the header for use in requests
headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']
}

# Place search here
# data = 'search "Halo Infinite"; fields *;'
data = 'fields *; limit 500;'

# print(headers)

top10 = requests.post('https://api.igdb.com/v4/games/', data=data, headers=headers )

top10data = top10.json()
# print(top10data)


# Insert JSON into our database

# GAMES STORES: 
#     game_id =           db.Column(db.Integer, primary_key=True)
#     title =             db.Column(db.String, nullable=False)
#     publisher =         db.Column(db.String, nullable=True)
#     description =       db.Column(db.String, nullable=True)
#     developer =         db.Column(db.String, nullable=True)
#     thumbnail_link =    db.Column(db.String, nullable=True)
#     release_date =      db.Column(db.DateTime, nullable=False)

global game_id
game_id = ""
global title
title = ""
global publisher
publisher = ""
global description
description = ""
global developer 
developer = ""
global thumbnail_link
thumbnail_link = ""
global release_date
release_date = date.today()

# create_game(self, game_id: int, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: date)



for x in top10data:
    # print(x)
    # print(x["id"])                    # GAME_ID
    game_id = x["id"]
    # print(x["name"])                  # TITLE
    title = x["name"]
    
    # print(x["summary"])               # DESCRIPTION
    try:
        descriptionLong = x["summary"]
        description = (descriptionLong[:997] + '..') if len(descriptionLong) > 997 else descriptionLong

    except Exception:
        pass
    # print(x["first_release_date"])    
    try:
        release_date = date.fromtimestamp(x["first_release_date"])  # RELEASE DATE
    except Exception:
        pass


    cover_data = 'fields url, width, height, image_id; where game = ' + str(x["id"]) + ';'

    cover = requests.post('https://api.igdb.com/v4/covers/', data=cover_data, headers=headers )
    cover_json = cover.json()
    # print(f"https://images.igdb.com/igdb/image/upload/t_cover_big/{cover_json[0]['image_id']}.png")

    try:
        thumbnail_link = "https://images.igdb.com/igdb/image/upload/t_cover_big/" + cover_json[0]['image_id'] + ".png"  # COVER ART
    except Exception:
        pass

    try:
        # For every company in the involved companies list, 
        for y in x["involved_companies"]:

            # query their company id, and whether or not they are a publisher or a developer
            involved_company_data = 'fields publisher, developer, company; where id = ' + str(y) + ';'
            involved_company = requests.post('https://api.igdb.com/v4/involved_companies/', data = involved_company_data, headers = headers)

            # convert to JSON to parse the data out of it
            involved_company_json = involved_company.json()

            # Note if this ID is for a publisher or a developer
            this_is_publisher = involved_company_json[0]["publisher"]
            this_is_developer = involved_company_json[0]["developer"]

            # search for the company name in the company table using the data we just got 
            company_data = "fields name; where id = " + str(involved_company_json[0]["company"]) + ';'
            # print(company_data)
            company = requests.post("https://api.igdb.com/v4/companies", data = company_data, headers=headers)

            # convert to JSON to parse the data out of it
            company_json = company.json()

            
            if (this_is_publisher): 
                # print(company_json[0]["name"])          # PUBLISHER
                try:
                    publisher = company_json[0]["name"]
                except Exception:
                    pass
            if (this_is_developer):
                # print(company_json[0]["name"])          # DEVELOPER
                try:
                    developer = company_json[0]["name"]
                except Exception:
                    pass
    except Exception:
        pass
    print("------------------------------------------------------------------")
    print(game_id, title, publisher, description, developer, thumbnail_link, release_date)
    with app.app_context():
        game_repository_singleton.create_game(game_id, title, publisher, description, developer, thumbnail_link, release_date)
