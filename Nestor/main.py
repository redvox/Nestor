import json
import weather
import my_calendar

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
    display.display(w, c)


if __name__ == '__main__':
    main()
