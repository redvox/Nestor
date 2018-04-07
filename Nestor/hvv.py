import requests

import main


def get_departures():
    hvv_config = main.read_config_file('hvv')
    headers = {'Content-Type': 'application/vnd.api+json'}
    try:
        r = requests.get('http://abfahrten.hvv.de/api/monitors/' + hvv_config['api_parameter'], headers=headers)
    except Exception:
        return []

    departures = r.json()["data"]["attributes"]["departures"]
    departure_list = []
    for departure in departures:
        if departure["direction"] == hvv_config['direction']:
            departure_list.append(departure)
        if len(departure_list) == 5:
            break
    return departure_list
