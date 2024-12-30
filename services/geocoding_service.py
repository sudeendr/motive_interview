import requests

NOMINATIN_URL='https://nominatim.openstreetmap.org/reverse'

def get_reverse_geocoding(lat,long):

    params={"lat":lat, "lon":long, "format": "json"}

    response=requests.get(NOMINATIN_URL, params=params)

    return response.json()


def get_address_from_coordinates(lat, lon):

    data = get_reverse_geocoding(lat, lon)

    return data.get("address", "Address not found")


#lat=52.5487429714954&lon=-1.81602098644987&zoom=18&addressdetails=1