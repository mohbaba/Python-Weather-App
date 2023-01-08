# Python Weather App
import flet
from flet import *
import requests
import datetime
import geopy
from geopy.geocoders import Nominatim


# Nominatim is an api that gets the data needed after getting the user's address
loc = Nominatim(user_agent = "Python Weather App")
location = str(input("Please type in your address, State and Country "))
getLoc = loc.geocode(location)
lat= getLoc.latitude
lon = getLoc.longitude



api_key = "b525ab6dd052055c4fc36e2ea7794cc4"
curremt = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon=-{lon}&exclude=hourly,daily&appid={api_key}')

days = [
    "Mon",
    "Tue",
    "Wed",
    "Thur",
    "Fri",
    "Sat",
    "Sun",
]

def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    c = Container(
        width = 310,
        height= 660
    )

if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")