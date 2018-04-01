import yaml
import weather
import display


def read_config_file():
    try:
        with open('./config/config.yaml') as config_file:
            return yaml.load(config_file)
    except KeyError as e:
        raise e


def main():
    config = read_config_file()
    w = weather.get_weather(config['weather']['api_key'], config['weather']['zmw'])
    # print(w)
    # w = {'temp': '4.8', 'feels_like': '5', 'icon': 'mostlycloudy', 'weather_icon': '\uf002',
    #      'today': {'high': '3', 'low': '-2', 'icon': 'partlycloudy', 'weather_icon': '\uf002',
    #                'conditions': 'Partly Cloudy'},
    #      'tomorrow': {'high': '8', 'low': '4', 'icon': 'mostlycloudy', 'weather_icon': '\uf031',
    #                   'conditions': 'Mostly Cloudy'}}
    display.display(w)


if __name__ == '__main__':
    main()
