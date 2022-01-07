# Importation des données via la méthode http.client
import http.client
import csv

conn = http.client.HTTPSConnection("jikan1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "jikan1.p.rapidapi.com",
    'x-rapidapi-key': "20013f0111msh6d05d5288cf7db6p1a1debjsn79fabb5d16d0"
    }

# Boucle pour récupérer les données sur les mangas
top_manga = []

def nbpagerequete(nb):
    for i in range(1,nb):
        conn.request("GET", "/top/manga/"+str(i)+"/manga", headers=headers)

        res = conn.getresponse()
        data = res.read()

        top_manga.append(data.decode("utf-8"))

nbpagerequete(10)
print(top_manga)

# Boucle pour récupérer les données sur les animes
# top_anime = []

# def nbpagerequete2(nb):
#     for i in range(1,nb):
#         conn.request("GET", "/top/anime/"+str(i)+"/favorite", headers=headers)

#         res = conn.getresponse()
#         data = res.read()

#         top_anime.append(data.decode("utf-8"))

# nbpagerequete2(10)
# print(top_anime)


# Exportation données format csv
with open('anime.csv', 'w', newline='') as file:
     mywriter = csv.writer(file)
     mywriter.writerows(top_manga)