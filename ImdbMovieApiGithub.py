import requests
import json

class Imdbfunctions():
    def __init__(self):
        self.web_url = "https://imdb-api.com/en/API/"
        self.api_key = "your_api_key"
        #you can get api key from imdb-api.com

    def getTop250Movies(self):
        web_url = self.web_url + "Top250Movies/" + self.api_key
        response = requests.get(web_url)
        return response.json()
    
    def getTop250Series(self):
        web_url = self.web_url + "Top250TVs/" + self.api_key
        response = requests.get(web_url)
        return response.json()
    
    def getMostPopularMovies(self):
        web_url = self.web_url + "MostPopularMovies/" + self.api_key
        response = requests.get(web_url)
        return response.json()
    
    def getMostPopularSeries(self):
        web_url = self.web_url + "MostPopularTVs/" + self.api_key
        response = requests.get(web_url)
        return response.json()
    
    def getInTheaters(self):
        web_url = self.web_url + "InTheaters/" + self.api_key
        response = requests.get(web_url)
        return response.json()
    
    def getComingSoon(self):
        web_url = self.web_url + "ComingSoon/" + self.api_key
        response = requests.get(web_url)
        return response.json()

    def getBoxOffice(self):
        web_url = self.web_url + "BoxOffice/" + self.api_key
        response = requests.get(web_url)
        return response.json()
    
    def searchMovie(self,expression):
        web_url = self.web_url + "SearchMovie/" + self.api_key + "/{0}".format(expression)
        response = requests.get(web_url)
        return response.json()
    
    def searchSeries(self,expression):
        web_url = self.web_url + "SearchSeries/" + self.api_key + "/{0}".format(expression)
        response = requests.get(web_url)
        return response.json()
    
    def searchEpisode(self,expression):
        web_url = self.web_url + "SearchEpisode/" + self.api_key + "/{0}".format(expression)
        response = requests.get(web_url)
        return response.json()
    
    def searchName(self,expression):
        web_url = self.web_url + "SearchName/" + self.api_key + "/{0}".format(expression)
        response = requests.get(web_url)
        return response.json()
    

imdb = Imdbfunctions()

while True:
    secim = input("1-Top 250 Movies\n2-Top 250 Series\n3-Most Popular Movies\n4-Most Popular Series\n5-In Theaters\n6-Coming Soon\n7-Box Office\n8-Search Movie\n9-Search Series\n10-Search Episode\n11-Search Name\nx- Exit\nSeciminiz: ")
    if secim == "x":
        break

    else:
        if secim == "1":
            result = imdb.getTop250Movies()
            for i in range(len(result["items"])):
                print(str(result["items"][i]["rank"])+"."+"{0}-{1}".format(result["items"][i]["fullTitle"],result["items"][i]["imDbRating"]))
            break

        elif secim == "2":
            result = imdb.getTop250Series()
            for i in range(len(result["items"])):
                print(str(result["items"][i]["rank"])+"."+"{0}-{1}".format(result["items"][i]["fullTitle"],result["items"][i]["imDbRating"]))
            break
        
        elif secim == "3":
            result = imdb.getMostPopularMovies()
            for i in range(len(result["items"])):
                print(str(result["items"][i]["rank"])+"."+"{0}-{1}".format(result["items"][i]["fullTitle"],result["items"][i]["imDbRating"]))
            break
            
        elif secim == "4":
            result = imdb.getMostPopularSeries()
            for i in range(len(result["items"])):
                print("{0}.{1}-{2}".format(str(result["items"][i]["rank"]),result["items"][i]["fullTitle"],result["items"][i]["imDbRating"]))
            break

        elif secim == "5":
            result = imdb.getInTheaters()
            for i in range(len(result["items"])):
                print("{0}.{1}-{2}-{3}".format(i+1,result["items"][i]["fullTitle"],result["items"][i]["imDbRating"],result["items"][i]["releaseState"]))
            break

        elif secim == "6":
            result = imdb.getComingSoon()
            for i in range(len(result["items"])):
                print("{0}.{1}-{2}".format(i+1,result["items"][i]["fullTitle"],result["items"][i]["releaseState"]))
            break
        
        elif secim == "7":
            result = imdb.getBoxOffice()
            for i in range(len(result["items"])):
                print("+{0}.{1}-{2}-{3}-{4}".format(i+1,result["items"][i]["title"],result["items"][i]["weekend"],result["items"][i]["gross"],result["items"][i]["weeks"]))
            break

        elif secim == "8":
            expression = input("expression: ")
            result = imdb.searchMovie(expression)
            length = len(result["results"])
            for i in range(length):
                print("{0}.{1}:{2}".format(i+1,result["results"][i]["title"],result["results"][i]["description"]))
            break

        elif secim == "9":
            expression = input("expression: ")
            result = imdb.searchSeries(expression)
            length = len(result["results"])
            for i in range(length):
                print("{0}.{1}:{2}".format(i+1,result["results"][i]["title"],result["results"][i]["description"]))
            break
            
        elif secim == "10":
            expression = input("expression: ")
            result = imdb.searchEpisode(expression)
            length = len(result["results"])
            print(f"results for {expression}")
            for i in range(length):
                print("{0}.{1}:{2}".format(i+1,result["results"][i]["title"],result["results"][i]["description"]))
            break

        elif secim == "11":
            expression = input("expression: ")
            result = imdb.searchName(expression)
            length = len(result["results"])
            print(f"results for {expression}")
            for i in range(length):
                print("{0}.{1}:{2}".format(i+1,result["results"][i]["title"],result["results"][i]["description"]))
            break

