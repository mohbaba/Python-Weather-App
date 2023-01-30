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


url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"

querystring = {"lon":lon,"lat":lat}

headers = {
	"X-RapidAPI-Key": "4fc5c694d7msha02ff297e54b089p15b409jsnd00a548ee6fe",
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

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
        current_feels = int(data['app_max_temp'])
        current_humidity = int(data['rh'])
        
        return [current_temp,current_weather,current_description, current_wind,current_humidity,current_feels]
        
    # current extra
    def current_extra():
        # For the extra information that will show on hover
        # Divide the visibility data by 1000 to get the value in km
        
        extra_info = []
        extra =[
            [
                int(data['vis']/ 1000),
                # Pass in extra data to display alongside the visibility
                "Km",
                "Visisbility",
                "./assets/visibility.png"
            ],
            [
                round(data['pres']*0.03,2),
                # Pass in extra data to display alongside the pressure
                "inHg",
                "Pressure",
                "./assets/barometer.png"
            ],
            [ # The final two are the sunrise and sunset, they will be converted from unix time to readable time using datetime functions
            # The fromtimestamp and the strftime function does...
            datetime.datetime.fromtimestamp(
                data["sunset_ts"]
            ).strftime("%I:%M %p"),
            "",
            "Sunset",
            "./assets/sunset.png",
            ],
            [ # The final two are the sunrise and sunset, they will be converted from unix time to readable time using datetime functions
            # The fromtimestamp and the strftime function does...
            datetime.datetime.fromtimestamp(
                data["sunrise_ts"]
            ).strftime("%I:%M %p"),
            "",
            "Sunrise",
            "./assets/sunrise.png",
            ]
            
            ]
        # Time to create UI using the extra data above 
        
        for datas in extra:
            extra_info.append(
                Container(
                    bgcolor="white10",
                    border_radius = 12,
                    alignment = alignment.center,
                    content=Column(
                        alignment = "center",
                        horizontal_alignment="center",
                        spacing = 15,
                        controls= [
                            Container(
                                alignment = alignment.center,
                                content = Image(
                                    src = datas[3],
                                    color = 'white'
                                ),
                                width = 30,
                                height = 30,
                            ),
                            Container(
                                content=Column(
                                    alignment = "center",
                                    horizontal_alignment="center",
                                    spacing = 5,
                                    controls = [
                                        Text(
                                            str(datas[0])+" " + datas[1],
                                            color = "white54",
                                            size = 14,
                                        ),
                                        Text(
                                            datas[2],
                                            color = "white54",
                                            size = 11,
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                    
                )
            )
        return extra_info
    
    
    # Animation
    def _expand(e):
        if e.data == "true":
            c.content.controls[1].height = 560
            c.content.controls[1].update()
        else:
            c.content.controls[1].height = 660 * 0.40
            c.content.controls[1].update()
    
    
    # Top container
    def _top():
        
        _today = current_temp()
        _today_extra = GridView(
            max_extent= 150,
            expand = 1,
            run_spacing= 5,
            spacing= 5
        )
        
        for info in current_extra():
            _today_extra.controls.append(info)
        
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
                                        text_align ='center',
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
                                            color = "white"
                                        ),
                                        Text(
                                            "wind",
                                            size = 9,
                                            color = "white"
                                        )
                                    ]
                                )
                            ),
                            Container(
                                content = Column(
                                    horizontal_alignment= "center",
                                    spacing = 2,
                                    controls = [
                                        Container(
                                            alignment = alignment.center,
                                            content = Image(src =" ./assets/humidity.png",
                                                            color = "white",
                                            ),
                                            width = 20,
                                            height =20,
                                        ),
                                        Text(
                                            str(_today[4]) + "%",
                                            size = 11,
                                            color = "white"
                                        ),
                                        Text(
                                            "Humidity",
                                            size = 9,
                                            color = "white"
                                        )
                                    ]
                                )
                            ),
                            
                            Container(
                                content = Column(
                                    horizontal_alignment= "center",
                                    spacing = 2,
                                    controls = [
                                        Container(
                                            alignment = alignment.center,
                                            content = Image(src =" ./assets/thermometer.png",
                                                            color = "white",
                                            ),
                                            width = 20,
                                            height =20,
                                        ),
                                        Text(
                                            str(_today[5]) + "°C",
                                            size = 11,
                                            color = "white"
                                        ),
                                        Text(
                                            "Feels Like",
                                            size = 9,
                                            color = "white"
                                        )
                                    ]
                                )
                            )
                        ]
                    ),
                    # to display more data on hover
                    _today_extra,
                ]
            )
            
            
        )
        return top
        
    # Bottom data
    def _bot_data():
        _bot_data = []
        for index in range(1,8):
            _bot_data.append(
                Row(
                    spacing=5,
                    alignment= 'spaceBetween',
                    controls = [
                        Row(
                            expand = 1,
                            alignment = 'start',
                            controls = [
                                Container(
                                    alignment = alignment.center,
                                    content = Text(
                                        
                                        days[
                                            datetime.datetime.weekday(
                                                datetime.datetime.fromtimestamp(
                                                    response.json()['data'][index]['ts']
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                        Row(
                            expand =1 ,
                            controls = [
                                Container(
                                    content=Row(
                                        alignment = 'start',
                                        controls = [
                                            Container(
                                                width=20,
                                                height = 20,
                                                alignment = alignment.center_left,
                                                content = Image(
                                                    # src = f'./assets/forecast/{response.json()['data'][index]["weather"]["main"].lower()}.png'
                                                )
                                            ),
                                            Text(
                                                response.json()['data'][index]["weather"]["main"],
                                                size=11,
                                                color='white54',
                                                text_align='center',
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                        Row(
                            expand = 1,
                            alignment = 'end',
                            controls=[
                                Container(
                                    alignment =alignment.center,
                                    content = Row(
                                        alignment = 'center',
                                        spacing = 5,
                                        controls=[
                                            Container(
                                                # we get the max temperature for that specific day
                                                
                                                width = 20,
                                                content = Text(
                                                    int(response.json()['data'][index]["max_temp"]),
                                                    text_align = 'start'
                                                ),
                                                
                                            
                                            )
                                        ]
                                    )
                                    
                                ),
                                Container(
                                    alignment =alignment.center,
                                    content = Row(
                                        alignment = 'center',
                                        spacing = 5,
                                        controls=[
                                            Container(
                                                # we get the min temperature for that specific day
                                                width = 20,
                                                content = Text(
                                                    int(response.json()['data'][index]["min_temp"]),
                                                    text_align = 'end' 
                                                ),
                                                
                                            )
                                        ]
                                    )
                                    
                                ),
                            ]
                        )
                    ]
                )
            )
        return _bot_data  
    
    # Bottom weather forecast
    
    def _bottom():
        _bot_column = Column(
            alignment="center",
            horizontal_alignment="center",
            spacing = 25,
            
        )
        
        for data in _bot_data():
            _bot_column.controls.append(data)
        
        
        bottom = Container(
            padding = padding.only(top=280, left=20, right=20, bottom=20),
            content = _bot_column
        )
        return bottom
    
    
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
            controls= [_bottom(),_top(),]
            
        )
    )
    page.add(c)

if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")