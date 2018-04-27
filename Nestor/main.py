import json
import argparse

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


def main(dry_run):
    config = read_config_file()
    # weather = wunderground.get_weather(config['weather'])
    events = gcalendar.calendar(config['calendar'])
    departures = hvv.get_departures(config['hvv'])

    display.render(weather=None,
                   calendar=events,
                   departures=departures,
                   dry_run=dry_run)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Nestor')
    parser.add_argument('-d', '--dry', action='store_true',
                        help='Do not use display, save image to file.')
    args = parser.parse_args()
    main(args.dry)
