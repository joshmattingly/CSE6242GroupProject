import config
import requests
import re


def geocode(address):

    address = str(address) + " Chicago, IL"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=" + config.api_key

    # parse json
    r = requests.get(url)
    data = r.json()

    for component in data['results'][0]['address_components']:
        if component['types'][0] == "locality":
            if component['long_name'] != 'Chicago':
                return geocode('1060 W Addision St')
        if component['types'][0] == 'postal_code':
            zipcode = component['short_name']

    formatted_address = data['results'][0]['formatted_address']
    lat = data['results'][0]['geometry']['location']['lat']
    long = data['results'][0]['geometry']['location']['lng']

    return formatted_address, lat, long, zipcode


def get_reps(address):

    address, lat, long, zipcode = geocode(address)
    url = "https://www.googleapis.com/civicinfo/v2/representatives?address=" + address + "&includeOffices=true&key=" + config.api_key

    senate = r'United States Senate'
    congress = r'United States House of Representatives IL-\d*'
    ward = r'Council\, Ward \d*'
    state_house = r'IL State House District \d*'
    state_senate = r'IL State Senate District \d*'

    # parse json
    r = requests.get(url)
    data = r.json()

    senator1 = []
    senator2 = []
    house_rep = []
    alderman = []
    state_rep = []
    state_senator = []

    try:
        for office in data['offices']:
            if re.search(senate, office['name']):
                senator1 = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
                senator2 = [data['officials'][office['officialIndices'][1]]['name'], data['officials'][office['officialIndices'][1]]['urls'][0]]
            if re.search(congress, office['name']):
                house_rep = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
            if re.search(ward, office['name']):
                alderman = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
            if re.search(state_house, office['name']):
                state_rep = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
            if re.search(state_senate, office['name']):
                state_senator = [data['officials'][office['officialIndices'][0]]['name'], data['officials'][office['officialIndices'][0]]['urls'][0]]
    except KeyError:
        return get_reps('1060 W Addison St, Chicago, IL 60613')

    return address, lat, long, zipcode, senator1, senator2, house_rep, state_senator, state_rep, alderman


if __name__ == '__main__':

    print(get_reps('4815 S Laflin St, Chicago, IL 60609'))
