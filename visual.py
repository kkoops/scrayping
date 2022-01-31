import matplotlib.pyplot as plt
import japanize_matplotlib
f = open('pokemonlistfile.txt', 'r')
data=f.read()
f.close()
katakana = [chr(i) for i in range(ord("ァ"), ord("ヺ")+1)]
count_list=[]
for i in katakana:
    print(i+':'+str(data.count(i)))
    count_list.append(data.count(i))
plt.bar(katakana,count_list)
plt.title('ポケモン名の文字出現頻度')
plt.show()
a=dict(zip(katakana,count_list))
b=sorted(a.items(),key=lambda x:x[1],reverse=True)
print(b)