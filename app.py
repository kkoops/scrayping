import urllib.request as req
from bs4 import BeautifulSoup
url="https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E4%B8%80%E8%A6%A7"
response=req.urlopen(url)
parse_html=BeautifulSoup(response,'html.parser')
r_list=parse_html.find_all('a')
non_pokemon_list=['ノーマル','ほのお','みず','でんき','くさ','こおり','かくとう',
'どく','じめん','ひこう','エスパー','むし','いわ','ゴースト','ドラゴン','あく','はがね','フェアリー','くさきのミノ',
'すなちのミノ',
'ゴミのミノ']
f = open('pokemonlistfile.txt', 'w')
#pokemon_count=0
list=list(dict.fromkeys(r_list))
for i  in range(11,len(list)-75):
    if (list[i].string not in non_pokemon_list and len(list[i].string)<=6):
        #print(list[i].string)
        f.write(list[i].string+'\n')
        #pokemon_count+=1
#print(pokemon_count)
