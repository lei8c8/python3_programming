my_url = "https://itunes.apple.com/search?term=Ann+Arbor&entity=podcast"

import requests 
import json
page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:50])
print(page.url)
x = page.json() #turn page.text into a python project
print(type(x))
print("------first item in the list------")
print(x[0])
print("------the whole list, pretty printed------")
print(json.dumps(x, indent=2))



kval_pairs = {'rel_rhy': 'funny'}
page2 = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page2.text[:150])
print(page.url)