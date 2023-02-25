import requests
import json


class NewsApi():
    def __init__(self):
        self.web_url = "https://newsapi.org/v2/"
        self.api_key = "your_api_key"
        # you can get api key from newsapi.com for free
    
    def getTopHeadlines(self,country):
        url = self.web_url + "top-headlines" + "?country=" + country + "&apiKey=" + self.api_key
        response = requests.get(url)
        return response.json()
    
    def searchKeyword(self,keyword):
        url = self.web_url + "everything" + "?q=" + keyword + "&apiKey=" + self.api_key
        response = requests.get(url)
        return response.json()
    
    def getBBCNews(self):
        url = self.web_url + "top-headlines" + "?sources=bbc-news" + "&apiKey=" + self.api_key
        response = requests.get(url)
        return response.json()
    
    def getEconomyNews(self,country):
        url = self.web_url + "top-headlines" + "?country=" + country + "&category=business" + "&apiKey=" + self.api_key
        response = requests.get(url)
        return response.json()
    
    def getSportNews(self,country):
        url = self.web_url + "top-headlines" + "?country=" + country + "&category=sport" + "&apiKey=" + self.api_key
        response = requests.get(url)
        return response.json()
    
    def getScienceNews(self,country):
        url = self.web_url + "top-headlines" + "?country=" + country + "&category=science" + "&apiKey=" + self.api_key
        response = requests.get(url)
        return response.json()
    
    def getPoliticNews(self,country):
        url = self.web_url + "top-headlines" + "?country=" + country + "&category=politics" + "&apiKey=" + self.api_key
        response = requests.get(url)
        return response.json()
    
    def getHealthNews(self,country):
        url = self.web_url + "top-headlines" + "?country=" + country + "&category=health" + "&apiKey=" + self.api_key
        response = requests.get(url)
        return response.json()
    
    def getTechnologyNews(self,country):
        url = self.web_url + "top-headlines" + "?country=" + country + "&category=technology" + "&apiKey=" + self.api_key
        response = requests.get(url)
        return response.json()

news = NewsApi()

while True:
    secim = input("1-Top Headlines\n2-Keyword Search\n3-BBC News\n4-Economy News\n5-Sport News\n6-Science News\n7-Politic News\n8-Health News\n9-Technology News\nx-Exit\nChoose: ")

    if secim == "x":
        break
    else:
        if secim == "1":
            country = input("country: ")
            with open("jsonfornewsapi.json","r") as file:
                file = json.load(file)
                country = file[country]

            result = news.getTopHeadlines(country)
            
            print("TOP HEADLINES".center(50,"*"))
            for i in range(len(result["articles"])):
                print("{0}.{1}--published at {2}".format(i+1,result["articles"][i]["title"],result["articles"][i]["publishedAt"]))
                url = result["articles"][i]["url"]
                print(f"more: {url}")
            

        elif secim == "2":
            keyword = input("keyword: ")
            result = news.searchKeyword(keyword)
            keyword = keyword.upper()
            print(f"RESULTS FOR {keyword}".center(50,"*"))
            length = len(result["articles"])
            print(f"{length} found...")

            for i in range(length):
                publishedat = result["articles"][i]["publishedAt"]
                title = result["articles"][i]["title"]
                content = result["articles"][i]["content"]
                url = result["articles"][i]["url"]
                print("".center(50,"*"))
                print(f"{i+1}.found:{publishedat}---{title}")
                print(f"{content}\n")
                print("more: "+url)
             
           
        elif secim == "3":
            
            result = news.getBBCNews()
            print("BBC NEWS".center(50,"*"))
            length = len(result["articles"])

            for i in range(length):
                publishedat = result["articles"][i]["publishedAt"]
                title = result["articles"][i]["title"]
                description = result["articles"][i]["description"]
                print("".center(50,"*"))
                print(f"{i+1}.found:{publishedat}---{title}")
                print(f"{description}")
        
        elif secim == "4":
            country = input("where?: ")
            with open("jsonfornewsapi.json","r") as file:
                file = json.load(file)
                country = file[country]
            
            result = news.getEconomyNews(country)
            print("ECONOMY NEWS".center(50,"*"))
            for i in range(len(result["articles"])):
                print("{0}.{1}--published at {2}".format(i+1,result["articles"][i]["title"],result["articles"][i]["publishedAt"]))
            
        elif secim == "5":
            country = input("where?: ")
            with open("jsonfornewsapi.json","r") as file:
                file = json.load(file)
                country = file[country]
            
            result = news.getSportNews(country)
            print("SPORT NEWS".center(50,"*"))
            for i in range(len(result["articles"])):
                print("{0}.{1}--published at {2}".format(i+1,result["articles"][i]["title"],result["articles"][i]["publishedAt"]))

        elif secim == "6":
            country = input("where?: ")
            with open("jsonfornewsapi.json","r") as file:
                file = json.load(file)
                country = file[country]
            
            result = news.getScienceNews(country)
            print("SCIENCE NEWS".center(50,"*"))
            for i in range(len(result["articles"])):
                print("{0}.{1}--published at {2}".format(i+1,result["articles"][i]["title"],result["articles"][i]["publishedAt"]))

        elif secim == "7":
            country = input("where?: ")
            with open("jsonfornewsapi.json","r") as file:
                file = json.load(file)
                country = file[country]
            
            result = news.getPoliticNews(country)
            print("POLITIC NEWS".center(50,"*"))
            for i in range(len(result["articles"])):
                print("{0}.{1}--published at {2}".format(i+1,result["articles"][i]["title"],result["articles"][i]["publishedAt"]))

        elif secim == "8":
            country = input("where?: ")
            with open("jsonfornewsapi.json","r") as file:
                file = json.load(file)
                country = file[country]
            
            result = news.getHealthNews(country)
            print("SCIENCE NEWS".center(50,"*"))
            for i in range(len(result["articles"])):
                print("{0}.{1}--published at {2}".format(i+1,result["articles"][i]["title"],result["articles"][i]["publishedAt"]))

            pass

        elif secim == "9":
            country = input("where?: ")
            with open("jsonfornewsapi.json","r") as file:
                file = json.load(file)
                country = file[country]
            
            result = news.getTechnologyNews(country)
            print("TECHNOLOGY NEWS".center(50,"*"))
            for i in range(len(result["articles"])):
                print("{0}.{1}--published at {2}".format(i+1,result["articles"][i]["title"],result["articles"][i]["publishedAt"]))
            pass
