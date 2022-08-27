import json
with open("task_2.json","r")as f:
    r=json.load(f)
def decade_movie_year():
    y=1955
    dic={}
    for i in range(y,2022,10):
        l=[]
        for j in r:
            if y<int(j) and int(j)<(y+10):
                l.append(r[j])
            dic[y]=l
            y+=10
        with open("task_3.json","w") as f:
            json.dump(dic,f,indent=5)
decade_movie_year()


# a=int(input("enterthe1stnumber"))
# b=int(input("enterthe2ndnumber"))
# c=int(input("enterthenumber3rd"))
# if a>b and a>c:
#     if b>c:
#         print(a,"max",b,"mid",c,"mim")
#     else:
#         print(a,"max",c,"mid",b,"mim")
# elif b>a and b>c:
#     if a>c:
#         print(b,"max",a,"mid",c,"min")
#     else:
#         print(b,"max",a,"mid",c,"mim")
# elif c>a and c>b:
#     if b>a:
#         print(c,"max",b,"mid",a,"mim")
#     else:
#         print(c,"max",a,"mid",b,"mim")
        
            
        



