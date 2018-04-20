import json
from datetime import datetime

import wunderground
import gcalendar
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
    weather = wunderground.get_weather(config['weather'])
    events = gcalendar.calendar(config['calendar'])
    departures = hvv.get_departures(config['hvv'])

    date_format = "%d-%m-%Y %H:%M"
    now = datetime.now().strftime(date_format)

    display.render(now, weather, events, departures)


if __name__ == '__main__':
    main()
