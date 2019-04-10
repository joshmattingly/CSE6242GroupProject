import config
import requests
import re


def get_reps(address):

    url = "https://www.googleapis.com/civicinfo/v2/representatives?address=" + address + "&includeOffices=true&key=" + config.api_key

    senate = r'United States Senate'
    congress = r'United States House of Representatives IL-\d*'
    county = r'County Commissioner\, District \d*'
    ward = r'Council\, Ward \d*'
    state_house = r'IL State House District \d*'
    state_senate = r'IL State Senate District \d*'

    # parse json
    r = requests.get(url)
    data = r.json()

    senator1 = []
    senator2 = []
    house_rep = []
    commissioner = []
    alderman = []
    state_rep = []
    state_senator = []

    for office in data['offices']:
        if re.search(senate, office['name']):
            senator1 = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
            senator2 = [data['officials'][office['officialIndices'][1]]['name'], data['officials'][office['officialIndices'][1]]['urls'][0]]
        if re.search(congress, office['name']):
            house_rep = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
        if re.search(county, office['name']):
            commissioner = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
        if re.search(ward, office['name']):
            alderman = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
        if re.search(state_house, office['name']):
            state_rep = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
        if re.search(state_senate, office['name']):
            state_senator = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]

    return senator1, senator2, house_rep, state_senator, state_rep, commissioner, alderman


def geocode(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(address) + "&key=" + config.api_key

    # parse json
    r = requests.get(url)
    data = r.json()

    formatted_address = ""
    lat = ""
    long = ""

    return [formatted_address, lat, long]


if __name__ == '__main__':
    print(get_reps('1060 W Addison St, Chicago, IL 60613'))
