# Utilisation méthode "request" pour récolter les données
# Ne fonctionne pas pour les animes
import requests
import json

headers = {
    'x-rapidapi-host': "jikan1.p.rapidapi.com",
    'x-rapidapi-key': "20013f0111msh6d05d5288cf7db6p1a1debjsn79fabb5d16d0"
    }

top = []

# On boucle pour avoir plusieurs pages
for page in range(1,11):
    url = "https://jikan1.p.rapidapi.com/top/manga/%s/manga" % page
    res = requests.request("GET", url, headers=headers)
    res_dict = json.loads(res.text)
    top_list = res_dict.get('top')
    for manga in top_list:
        # On récupère les clés qui nous intéressent
        # keys = ['mal_id', 'rank', 'title', 'url', 'image_url', 'volumes', 'start_date', 'end_date', 'members', 'score']
        top.append({key: manga[key] for key in ['mal_id', 'rank', 'title', 'score']})

print(type(top))
print(type(res_dict))
print(top)