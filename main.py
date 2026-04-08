import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
# EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
# EMAIL_PASSWORD =os.getenv("EMAIL_PASSWORD")

def get_weather(city): #we are writing a function so we can resue it to accept multiple cities
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial" #this line of code will behave as an endpoint, it will get the data from the url
    response = requests.get(url) #will send a request to the api to get the data response

    if response.status_code == 200: #using an if statement to error handle our response statuses
        data = response.json() 
        return data #will send weather data back to whoever called the function
    else:
        print(f"Failed to retrieve data. {response.status_code}")



location = input("What town would you like to choose? ") # asking user for location variable
weather_info = get_weather(location) #calling our function and passing location

if weather_info:
    print(f"Location: {weather_info['name']}")
    print(f"Current Temperature: {weather_info['main']['temp']}°F")
    print(f"Conditions: {weather_info['weather'][0]['main']}")
    
    


