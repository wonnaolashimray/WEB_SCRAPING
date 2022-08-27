
import json
from bs4 import BeautifulSoup
import requests
page=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(page.text,"html.parser")
def scrap_top_list():
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")
    
    movie_ranks=[]
    movie_name=[]
    year_of_release=[]
    movie_urls=[]
    movie_ratings=[]
    
    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=""
        for i in position:
            if "." not in i:
                rank=rank+i
            else:
                break
        movie_ranks.append(rank)
        
        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)
        
        year=tr.find("td",class_="titleColumn").span.get_text()
        year_of_release.append(year)
        
        imdb_rating=tr.find("td",class_="ratingColumn").strong.get_text()
        movie_ratings.append(imdb_rating)
        
        link=tr.find("td",class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com"+link
        movie_urls.append(movie_link)
    top_movies=[]
    details={"position":"","name":"","year":"","rating":"","url":""}
    for i in range(0,len(movie_ranks)):
        details["position"]=int(movie_ranks[i])
        details["name"]=str(movie_name[i])
        year_of_release[i]=year_of_release[i][1:5]
        details["year"]=int(year_of_release[i])
        details["rating"]=float(movie_ratings[i])
        details["url"]=movie_urls[i]
        top_movies.append(details.copy())
    with open("imdb 1_task.json","w") as f:
        json.dump(top_movies,f,indent=4)
scrap_top_list()






