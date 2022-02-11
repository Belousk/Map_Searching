import requests

GEOCODER_API_SERVER = "https://geocode-maps.yandex.ru/1.x/"
SEARCH_API_SERVER = "https://search-maps.yandex.ru/v1/"
MAP_API_SERVER = "https://static-maps.yandex.ru/1.x/"


def get_address_coords(address: str):
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"}
    r = requests.get(GEOCODER_API_SERVER, params=geocoder_params)
    json_r = r.json()
    toponym = json_r["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    return toponym["Point"]["pos"].split()


def save_image(coords: (str, str), z: int, filename: str):
    map_params = {
        "l": "map",
        "ll": ",".join(coords),
        "z": z
    }
    response = requests.get(MAP_API_SERVER, params=map_params)
    with open(filename, 'wb') as file:
        file.write(response.content)
