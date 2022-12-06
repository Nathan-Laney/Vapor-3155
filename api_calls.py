import requests
from models import db
from datetime import date
import time
from src.repositories.tag_repository import tag_repository_singleton
from dotenv import load_dotenv
from os import getenv
from src.repositories.game_repository import game_repository_singleton
from src.repositories.tag_game_repository import tag_game_repository_singleton

# REMOVE FOR FRONTEND TO WORK 
# from app import app

# GAMES STORES: 
#     game_id =           db.Column(db.Integer, primary_key=True)
#     title =             db.Column(db.String, nullable=False)
#     publisher =         db.Column(db.String, nullable=True)
#     description =       db.Column(db.String, nullable=True)
#     developer =         db.Column(db.String, nullable=True)
#     thumbnail_link =    db.Column(db.String, nullable=True)
#     release_date =      db.Column(db.DateTime, nullable=False)

load_dotenv()
keys = {}
client_id = getenv('IGDB_CLIENT_ID')
client_secret = getenv('IGDB_CLIENT_SECRET')

# if (keys['expires_in'] < 1000):
#     keys = authorize()

expires_on = time.time()


def authorize():
    global keys
    global client_id
    global client_secret
    global expires_on

    body = {
        'client_id': client_id,
        'client_secret': client_secret,
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)

    # Outputs the given access token 
    keys = r.json()

    #update time to live of access token
    expires_on = time.time() + keys['expires_in']
    print(f"Expires on {expires_on}")

    return keys


def search_db(query:str):
    game_id = ""
    title = ""
    publisher = ""
    description = ""
    developer = ""
    thumbnail_link = ""
    release_date = date.today()
    global keys
    global client_id
    global expires_on

    if (time.time() > expires_on - 60):
        keys = authorize()
    
    # Gens the header for use in requests
    headers = {
        'Client-ID': client_id,
        'Authorization': 'Bearer ' + keys['access_token']
    }

    # Place search here
    data = f'search "{query}"; fields *;'
    # data = 'fields *; where rating > 75; where category = 0; where status = 0; sort rating desc; limit 100;'

    # print(headers)

    result = requests.post('https://api.igdb.com/v4/games/', data=data, headers=headers )

    result_json = result.json()

    print(result_json)
    # Insert JSON into our database

    for x in result_json:
        # print(x)
        # print(x["id"])                    # GAME_ID
        game_id = x["id"]
        # print(x["name"])                  # TITLE
        title = x["name"]
        
        # print(x["summary"])               # DESCRIPTION
        try:
            descriptionLong = x["summary"]
            description = (descriptionLong[:996] + '...') if len(descriptionLong) > 996 else descriptionLong

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
        # print("------------------------------------------------------------------")
        # print(game_id, title, publisher, description, developer, thumbnail_link, release_date)
        game_repository_singleton.create_game(game_id, title, publisher, description, developer, thumbnail_link, release_date)

        # Add game's Themes and Genres to the tag_game table
        try:
            for i in x['genres']:
                tag_game_repository_singleton.create_tag_game(i, x['id'])
        except Exception:
            pass

def populate_tags():
    global keys
    global client_id
    global expires_on

    # https://api.igdb.com/v4/genres

    # check validity of keys
    if (time.time() > expires_on - 60):
        keys = authorize()
    
    # Gens the header for use in requests
    headers = {
        'Client-ID': client_id,
        'Authorization': 'Bearer ' + keys['access_token']
    }

    # Place search here
    data = 'fields name, id; limit 100;'
    # data = 'fields *; where rating > 75; where category = 0; where status = 0; sort rating desc; limit 100;'

    # print(headers)

    themes = requests.post('https://api.igdb.com/v4/themes/', data=data, headers=headers )
    genres = requests.post('https://api.igdb.com/v4/genres/', data=data, headers=headers )
    themes_json = themes.json()
    genres_json = genres.json()
    for x in themes_json:
        tag_repository_singleton.create_tag(x['id'], x['name'])
    for x in genres_json:
        tag_repository_singleton.create_tag(x['id'], x['name'])


