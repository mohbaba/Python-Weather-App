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
print(lat)
print(lon)