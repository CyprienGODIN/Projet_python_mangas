# Importation
import csv
import pprint

# CSV -> dictionnaire    
# keys = ['mal_id', 'rank', 'title', 'url', 'image_url', 'type', 'episodes', 'start_date', 'end_date', 'members', 'score']
reader = csv.DictReader(open('anime.csv', 'r'))
dict_list = []
for line in reader:
    dict_list.append(line)
pprint.pprint(dict_list)