import config
import requests
import json


def get_reps(address):
    url = "https://www.googleapis.com/civicinfo/v2/representatives?address=" + address + \
            "&includeOffices=true&levels=administrativeArea1&levels=country&key=" + config.api_key
    # parse json
    r = requests.get(url)
    data = r.json()

    senator1 = ""
    senator2 = ""
    house_rep = ""
    state_senator = ""
    state_rep = ""

    return [senator1, senator2, house_rep, state_senator, state_rep]


def geocode(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(address) + "&key=" + config.api_key

    # parse json
    r = requests.get(url)
    data = r.json()

    formatted_address = ""
    lat = ""
    long = ""

    return [formatted_address, lat, long]
