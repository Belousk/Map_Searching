from typing import List

import requests

GEOCODER_API_SERVER = "https://geocode-maps.yandex.ru/1.x/"
SEARCH_API_SERVER = "https://search-maps.yandex.ru/v1/"
MAP_API_SERVER = "https://static-maps.yandex.ru/1.x/"


def get_address_coords(address: str) -> List[int]:
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"}
    r = requests.get(GEOCODER_API_SERVER, params=geocoder_params)
    json_r = r.json()
    toponym = json_r["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    coords_str = toponym["Point"]["pos"].split(',')
    return [int(coords_str[0]), int(coords_str[1])]


def save_image(coords: (int, int), z: int, filename: str):

    map_params = {
        "l": "map",
        "ll": f'{coords[0]},{coords[1]}',
        "z": z
    }
    response = requests.get(MAP_API_SERVER, params=map_params)
    with open(filename, 'wb') as file:
        file.write(response.content)
