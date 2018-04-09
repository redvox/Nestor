import json
from datetime import datetime

import weather
import my_calendar
import hvv

import display


def read_config_file():
    try:
        with open('./config/config.json') as config_file:
            return json.load(config_file)
    except KeyError as e:
        raise e


def main():
    config = read_config_file()
    weather_data = weather.get_weather(config['weather'])
    calendar_events = my_calendar.calendar(config['calendar'])
    departures = hvv.get_departures(config['hvv'])

    date_format = "%d-%m-%Y %H:%M"
    now = datetime.now().strftime(date_format)

    display.display(now, weather_data, calendar_events, departures)


if __name__ == '__main__':
    main()
