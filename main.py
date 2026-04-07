import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD =os.getenv("EMAIL_PASSWORD")

def get_weather(city): #we are writing a function so we can resue it to accept multiple cities
    url = f"" #this line of code will behave as an endpoint, it will get the data from the url
    response = requests.get(url) #will send a request to the api to get the data response
    data = response.json() 
    return data #will send weather data back to whoever called the function


