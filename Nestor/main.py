import json
import weather
import my_calendar


# import display


def read_config_file(name):
    try:
        with open('./config/{}_config.json'.format(name)) as config_file:
            return json.load(config_file)
    except KeyError as e:
        raise e


def main():
    # weather_config = read_config_file('weather')
    # w = weather.get_weather(weather_config['api_key'], weather_config['zmw'])
    # print(w)
    w = {'temp': '4.8', 'feels_like': '5', 'icon': 'mostlycloudy', 'weather_icon': '\uf002',
         'today': {'high': '3', 'low': '-2', 'icon': 'partlycloudy', 'weather_icon': '\uf002',
                   'conditions': 'Partly Cloudy'},
         'tomorrow': {'high': '8', 'low': '4', 'icon': 'mostlycloudy', 'weather_icon': '\uf031',
                      'conditions': 'Mostly Cloudy'}}

    calendar_config = read_config_file('calendar')
    my_calendar.calendar(calendar_config)

    # display.display(w)


if __name__ == '__main__':
    main()
