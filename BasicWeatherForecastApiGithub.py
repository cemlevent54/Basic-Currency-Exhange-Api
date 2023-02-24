import requests
import json

class WeatherForecast():
    def __init__(self):
        self.api_url = "http://api.weatherstack.com/"
        self.api_key = "Your_api_key"
        #you can get api key from weatherstack
        self.api_url2 = "http://api.weatherbit.io/v2.0/forecast/daily"
        self.api_key2 = "Your_api_key_2"
        #you can get api key from weatherbit.io
        

    def current_weather(self,location):
        response = requests.get(f"{self.api_url}/current?access_key={self.api_key}&query={location}")
        return response.json()

    def daily_weather(self,location):
        url = self.api_url2 + "?city=" + location + ",&key=" + self.api_key2
        response = requests.get(url)
        return response.json()
    
weatherF = WeatherForecast() 

while True:
    secim = input("1-Current weather your location\n2- Daily max,min weather forecast\nx- Exit\nSeciminiz: ")

    if secim == "x":
        break
    else:
        if secim == "1":
            location = input("location: ")
            weathers = weatherF.current_weather(location)
            degree = weathers["current"]["temperature"]
            description = weathers["current"]["weather_descriptions"]
            description = description[0]
            observationtime = weathers["current"]["observation_time"]
            print(f"At {observationtime}, {degree} degrees Celcius and {description}")
            
        elif secim == "2":
            location = input("location: ")
            result = weatherF.daily_weather(location)
            currentweather = result["data"][0]["temp"]
            max_temperature = result["data"][0]["high_temp"]
            min_temperature = result["data"][0]["low_temp"]
            weather = result["data"][0]["weather"]["description"]

            print(currentweather)
            print(f"max temperature in {location}: {max_temperature}")
            print(f"min temperature in {location}: {min_temperature}")
            print(weather)