import requests
import json
from bs4 import BeautifulSoup
with open("imdb 1_task.json","r") as f:
    a=json.load(f)
    i=0
    url=[]
    while i<len(a):
        print(i+1,":",a[i]["name"])
        url.append(a[i]["url"])
        i=i+1
    user=int(input("enter the movie sl.No  :"))-1
    x=url[user]
    b=requests.get(x)
    soup=BeautifulSoup(b.text,"html.parser")
    c=soup.find('script',type='application/ld+json').text
    a=json.loads(c)
    print(b)
    with open("try.json","w") as f:
        json.dump(a,f,indent=2)
    with open("try.json","r") as k:
        r=json.load(k)
    dic={}
    for j in r:
        dic['name']=r['name']
        dic['director']=[r['director'][0]['name']]
        dic['image']=r['image']
        dic['description']=r['description']
        dic["language"]=r['review']['inLanguage']
        dic['genre']=r['genre']
        dic['country']='india'
    with open("imbd 4_task.json","w") as f:
        json.dump(dic,f,indent=2)



