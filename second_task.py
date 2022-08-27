import json
with open("imdb 1_task.json","r") as f:
        y=json.load(f)
def movie_same_year():
    d={}
    for i in y:
        l=[]
        year=i["year"]
        if year not in d  :
            for j in y:
                if year==j["year"]:
                    l.append(j)
                d[year]=l
            # print(d)
    with open("task_2.json","w") as x:
        json.dump(d,x,indent=5, sort_keys=True)
        
movie_same_year()
    

