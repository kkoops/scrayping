def count_index(word,str_g):
    count=0
    for i in range(5):
        if str_g[i]==word[i]:
            count=count+1
    return count
def count_max_length(str_g):
    count=0
    for i in range(5):
        if str_g[i] is not None:
            count=count+1
    return count
def count_not_match(word,str_b):
    count=0
    for alp in str_b:
        if alp in word:
            count=count+1
    return count==0
def count_match(word,str_y):
    count=0
    for alp in str_y:
        if alp in word:
            count=count+1
    return count==len(str_y)
pokemon_list=[]
black=[]
yellow=['ー','ン','ラ','']
green=[None,None,None,None,None]
maxlength=count_max_length(green)

with open('pokemonlistfile.txt') as f:
    lines=f.read()
    for i in lines.split("\n"):
       pokemon_list.append(i)
for i in pokemon_list:
    if len(i)==5  and count_index(i,green)==maxlength and count_not_match(i,black)==True and count_match(i,yellow)==True:
        print(i)
    