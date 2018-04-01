import requests
import json
from pprint import pprint


class Weather:
    temp = 0
    feels_like = 0

    def __init__(self):
        pass


def get_weather(api_key, zmw):
    base_url = 'http://api.wunderground.com/api/{api_key}/{method}/q/zmw:{zmw}.json'
    current_url = base_url.format(api_key=api_key, method='conditions', zmw=zmw)
    forecast_url = base_url.format(api_key=api_key, method='forecast', zmw=zmw)

    current_weather_response = requests.get(current_url)
    current_weather = json.loads(current_weather_response.text).get('current_observation')
    pprint("current_weather")
    pprint(current_weather)

    forecast_weather_response = requests.get(forecast_url)
    forecast_weather = json.loads(forecast_weather_response.text) \
        .get('forecast') \
        .get('simpleforecast') \
        .get('forecastday')
    pprint("forecast_weather")
    pprint(forecast_weather)

    weather = {
        'temp': str(current_weather['temp_c']),
        'feels_like': current_weather['feelslike_c'],
        'icon': current_weather['icon'],
        'weather_icon': get_weather_icon(current_weather['icon']),
        'today': {
            'high': forecast_weather[0]['high']['celsius'],
            'low': forecast_weather[0]['low']['celsius'],
            'icon': forecast_weather[0]['icon'],
            'weather_icon': get_weather_icon(forecast_weather[0]['icon']),
            'conditions': forecast_weather[0]['conditions']
        },
        'tomorrow': {
            'high': forecast_weather[1]['high']['celsius'],
            'low': forecast_weather[1]['low']['celsius'],
            'icon': forecast_weather[1]['icon'],
            'weather_icon': get_weather_icon(forecast_weather[1]['icon']),
            'conditions': forecast_weather[1]['conditions']
        }
    }
    # pprint(weather)
    return weather


def get_weather_icon(condition):
    icons_list = {'chancerain': '',
                  'chancesleet': '',
                  'chancesnow': '',
                  'chancetstorms': '',
                  'clear': '',
                  'flurries': '',
                  'fog': '',
                  'hazy': '',
                  'mostlycloudy': '',
                  'mostlysunny': '',
                  'partlycloudy': '',
                  'partlysunny': '',
                  'sleet': '',
                  'rain': '',
                  'sunny': '',
                  'tstorms': '', 'cloudy': ''}
    return icons_list.get(condition, '?')


def geo_lookup():
    lookup_weather_response = requests.get(
        "http://api.wunderground.com/api/6c03ed0600620ee4/geolookup/q/Germany/Hamburg.json")
    lookup = json.loads(lookup_weather_response.text)
    pprint(lookup)
