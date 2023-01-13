# Python Weather App
import flet
from flet import *
import requests
import datetime
import geopy
from geopy.geocoders import Nominatim
import json


# Nominatim is an api that gets the data needed after getting the user's address
# loc = Nominatim(user_agent = "Python Weather App")
# location = str(input("Please type in your address, State and Country "))
# getLoc = loc.geocode(location)
# lat= getLoc.latitude
# lon = getLoc.longitude
lat = 8.8367891
lon = 4.6688487


url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"lon":lon,"lat":lat}

headers = {
	"X-RapidAPI-Key": "4fc5c694d7msha02ff297e54b089p15b409jsnd00a548ee6fe",
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

api_key = "c18e814df3b2496ab089376f69dfc493"
current = requests.get(f'https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={api_key}&include=minutely')
data = response.json()['data'][0]


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
    
    
    # current temperature
    def current_temp():
        # The int function will round the temp to the a whole figure
        current_temp = int(data['temp'])
        current_description = str(data['weather']['description'])
        current_weather = data['weather']['code']
        current_wind = int(data['wind_spd'])
        current_feels = int(data['app_temp'])
        current_humidity = int(data['rh'])
        
        
        
        return [current_temp,current_weather,current_description, current_wind,current_humidity,current_feels]
        
    
    
    # Animation
    def _expand(e):
        if e.data == "true":
            c.content.controls[0].height = 560
            c.content.controls[0].update()
        else:
            c.content.controls[0].height = 660 * 0.40
            c.content.controls[0].update()
    
    
    # Top container
    def _top():
        
        _today = current_temp()
        
        top = Container(
            width = 330,
            height= 660 * 0.40,
            gradient= LinearGradient(
                begin= alignment.bottom_left,
                end= alignment.top_right,
                colors= ["lightblue600", "lightblue900"],
            ),
            border_radius= 28,
            animate = animation.Animation(duration=450,curve="decelerate"),
            on_hover=lambda e: _expand(e),
            content=Column(
                alignment = "start",
                spacing = 10,
                controls= [
                    Row(
                        alignment= "center",
                        controls = [
                            Text(
                                "Kwara, NG",
                                size = 16,
                                weight = "w500",
                                color = "white"
                                )
                            ]
                        ),
                    Container(padding = padding.only(bottom=5)),
                    Row(
                        alignment= 'center',
                        spacing = 30,
                        controls = [
                            Column(
                                controls = [
                                    Container(
                                        width= 90,
                                        height =90,
                                        image_src = "./assets/cloudy-day.png"
                                    )
                                ]
                            ),
                            Column(
                                spacing = 5,
                                horizontal_alignment= "center",
                                controls = [
                                    Text(
                                        "Today",
                                        size = 12,
                                        text_align = 'center',
                                        color= "white"
                                    ),
                                    Row(
                                        vertical_alignment = 'start',
                                        spacing = 0,
                                        controls = [
                                            Container(
                                                content = Text(
                                                    _today[0],
                                                    size = 52,
                                                    color= "white"
                                                    
                                                )
                                            ),
                                            Container(
                                                content = Text(
                                                    "°C",
                                                    size = 28,
                                                    text_align= 'center',
                                                    color = "white"
                                                    
                                                )
                                            )
                                        ]
                                    ),
                                    Text(
                                        str(_today[2]) + ' -Overcast',
                                        size = 10,
                                        color = "white",
                                        text_align= 'center'
                                    )
                                ]
                            )
                        ]
                    ),
                    Divider(
                        height = 8,
                        thickness = 1,
                        color= "white10",
                    ),
                    Row(
                        alignment = "spaceAround",
                        controls = [
                            Container(
                                content = Column(
                                    horizontal_alignment= "center",
                                    spacing = 2,
                                    controls = [
                                        Container(
                                            alignment = alignment.center,
                                            content = Image(src =" ./assets/wind.png",
                                                            color = "white",
                                            ),
                                            width = 20,
                                            height =20,
                                        ),
                                        Text(
                                            str(_today[3]) + " km/hr",
                                            size = 11,
                                        )
                                        Text(
                                            "wind",
                                            size = 9,
                                            color = "white54"
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
            
            
        )
        return top
        
    
    
    # This container is root container where all the different sub roots or functions will be stacked.
    # It could be regarded as the main app
    c = Container(
        width = 310,
        height= 660,
        border_radius= 35,
        bgcolor= "black",
        padding= 10,
        content= Stack(
            width= 300,
            height= 550,
            controls= [_top(),]
            
        )
    )
    page.add(c)

if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")