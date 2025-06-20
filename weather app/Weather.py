import socket
import requests
import json

# Python Program to Get IP Address


def ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return str(IPAddr)

# Fetch today's weather


def weather(city):
    try:
        res = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key=b1c3786cab0044dc9e955900230407&q={city}&aqi=no")
        data = json.loads(res.text)
        try:
            if data['error']:
                print(f"\nError: {data['error']['message']}\n")
        except:
            print(f'''\n           -----> Location {data['location']['name']}, {data['location']['region']},{data['location']['country']}
           -----> Current Time: {data['location']['localtime']}
           -----> Tempreture (celcius): {data['current']['temp_c']}
           -----> Current condition:  {data['current']['condition']['text']}
           -----> Wind speed (Kilometer per hour): {data['current']['wind_kph']}
           -----> Wind Angle (degree): {data['current']['wind_degree']}
           -----> Wind Direction: {data['current']['wind_dir']}
           -----> Pressure (mb): {data['current']['pressure_mb']}
           -----> Cloud: {data['current']['cloud']}\n
      ''')
            forecast(city)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Fuction to fetch next five day weather


def forecast(city):
    try:
        res = requests.get(
            f"http://api.weatherapi.com/v1/forecast.json?key=b1c3786cab0044dc9e955900230407&q={city}&days=7")
        data = json.loads(res.text)
        try:
            if data['error']:
                print(f"\nError: {data['error']['message']}\n")
        except:
            print("\n\n           ***** Next Five Days Weather *****")
            for i in range(0, 6):

                print(f'''\n           -----> Location {data['location']['name']}, {data['location']['region']},{data['location']['country']}
           -----> Date: {data['forecast']['forecastday'][i]['date']}
           -----> Maximum Tempreture (celcius): {data['forecast']['forecastday'][i]['day']['maxtemp_c']}
           -----> Minimum tempreture:  {data['forecast']['forecastday'][i]['day']['mintemp_c']}
           -----> Average Tempreture: {data['forecast']['forecastday'][i]['day']['avgtemp_c']}
           -----> Maximum Wind (KPH): {data['forecast']['forecastday'][i]['day']['maxwind_kph']}
           -----> Condition: {data['forecast']['forecastday'][i]['day']['condition']['text']}
      ''')
                print(
                    "---------------------------------------------------------------------------")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Chosing right city fuction


def City():
    try:
        choice = input(
            "\nWhat's the name of your city type correct full name or some starting words? ").strip()
        res = requests.get(
            f"https://api.weatherapi.com/v1/search.json?key=b1c3786cab0044dc9e955900230407&q={choice}")
        li_data = json.loads(res.text)

        if li_data == []:
            print('\n  (>_<) Invalid choice')
            City()
        else:
            i = 1
            for data in li_data:
                print(f'''
    {i}. {data['name']}, {data['region']}, {data['country']} ''')
                i = i + 1
            choice = int(input(
                f"\nChoose your city number from 1 to {i-1} if not found your city Type 0: "))
            if choice == 0:
                City()
            return li_data[choice-1]['name']
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
