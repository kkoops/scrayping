pokemon_list=[]
black=[]
yellow=[]
green=[]
with open('pokemonlistfile.txt') as f:
    lines=f.read()
    for i in lines.split("\n"):
       pokemon_list.append(i)
#print(pokemon_list)
for i in pokemon_list:
    if ('ン' in i and 'ル'in i and 'ラ' in i and 'ス'in i):
        print(i)
    