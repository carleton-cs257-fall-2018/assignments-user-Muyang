import requests
import sys

# take off the apikey from code!!!

print("***************************************************************************************************")
search_artist = input("Which artist would you like to search? ")
print("***************************************************************************************************")
r = requests.get("http://api.musixmatch.com/ws/1.1/artist.search",
    params = {"apikey": "06bc14094277cad45208f53970a03311", "q_artist": str(search_artist)})
    # make q_artist another inputted value
artist_id_list = []
empty = None

print(r.url)
print("***************************************************************************************************")

for j in r.json()["message"]["body"]["artist_list"]:
    print(j['artist']['artist_id'], j['artist']['artist_name'])
    artist_id_list.append(j['artist']['artist_id'])

print("***************************************************************************************************")
artist_id = input("Which artist_id would you like to search? ")
print("***************************************************************************************************")
for j in r.json()["message"]["body"]["artist_list"]:
    if j['artist']['artist_id'] == int(artist_id):
        empty = j

print("Result for artist_id ", artist_id, ":",empty['artist']['artist_name'])
for info in empty['artist'].keys():
    print(info, ":  ", empty['artist'][info])
