import requests


def get_departures(config):
    headers = {'Content-Type': 'application/vnd.api+json'}
    try:
        r = requests.get('http://abfahrten.hvv.de/api/monitors/' + config['api_parameter'], headers=headers)
    except Exception:
        return []

    departures = r.json()["data"]["attributes"]["departures"]
    departure_list = []
    for departure in departures:
        if departure["direction"] == config['direction']:
            departure_list.append(departure)
        if len(departure_list) == 5:
            break
    return departure_list
