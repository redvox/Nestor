import json
from datetime import datetime

import os
import weather
import my_calendar
from pprint import pprint
import hvv


import display


def read_config_file(name):
    try:
        with open('./config/{}_config.json'.format(name)) as config_file:
            return json.load(config_file)
    except KeyError as e:
        raise e


def main():
    weather_config = read_config_file('weather')
    w = weather.get_weather(weather_config['api_key'], weather_config['zmw'])

    calendar_config = read_config_file('calendar')
    c = my_calendar.calendar(calendar_config)

    date_format = "%d-%m-%Y %H:%M"
    now = datetime.now().strftime(date_format)

    departures = hvv.get_departures()

    display.display(now, w, c, departures)


if __name__ == '__main__':
    main()
