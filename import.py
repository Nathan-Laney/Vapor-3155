import requests
from models import db

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
data = 'search "Halo"; fields name;'

print(headers)

top10 = requests.post('https://api.igdb.com/v4/games/', data=data, headers=headers )

top10data = top10.json()
print(top10data)


# Convert JSON into our database

