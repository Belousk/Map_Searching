from typing import List, Tuple

import requests

GEOCODER_API_SERVER = "https://geocode-maps.yandex.ru/1.x/"
SEARCH_API_SERVER = "https://search-maps.yandex.ru/v1/"
MAP_API_SERVER = "https://static-maps.yandex.ru/1.x/"


def get_address_coords(address: str) -> Tuple[float, float]:
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"}
    r = requests.get(GEOCODER_API_SERVER, params=geocoder_params)
    json_r = r.json()
    toponym = json_r["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    coords_str = toponym["Point"]["pos"].split(' ')
    return float(coords_str[0]), float(coords_str[1])


def save_image(coords: List[float], z: int, filename: str, map_type: str, address_pos: Tuple[float, float]) -> None:
    map_params = {
        "l": map_type,
        "ll": f'{coords[0]},{coords[1]}',
        "z": z,
        "pt": f'{address_pos[0]},{address_pos[1]},flag'
    }
    response = requests.get(MAP_API_SERVER, params=map_params)
    with open(filename, 'wb') as file:
        file.write(response.content)
