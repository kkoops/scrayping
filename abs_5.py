g = open('only5pokemonlistfile.txt', 'w')
with open('pokemonlistfile.txt','r') as f:
    lines=f.read()
    for i in lines.split("\n"):
       if(len(i)==5):
            g.write(i+'\n')