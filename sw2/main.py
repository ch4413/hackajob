import urllib.request
import json


def get_json(url_string):
    """
        data (json) json from url address
    Args:
        url_string (string) valid url string
    Returns:
        data (json) json from url address
    """
    with urllib.request.urlopen(url_string) as url:
        data = json.loads(url.read().decode())
    return data


def clean_name(name):
    """
    Returns string of characters in film passed
    Args:
        name (string) string value
    Returns:
        formatted string replacing spaces with %20
    """
    return name.replace(' ', '%20')


def get_films(character):
    """
    Returns string of characters in film passed
    Args:
        character (string) string of Star Wars character.
    Returns:
        res (string) formatted string starting with character and followed by ordered list of films

    """
    name = clean_name(character)
    url = 'https://challenges.hackajob.co/swapi/api/people/?search=' + name
    json_data = get_json(url)
    if len(json_data['results']) == 0:
        res = character + ': none'
    else:
        film_urls = json_data['results'][0]['films']
        film_names = [get_json(x)['title'] for x in film_urls]
        film_names.sort()
        res = character + ': ' + ', '.join(film_names)
    return res


def get_characters(film):
    """
    Returns string of characters in film passed
    Args:
        film (string) string of Star Wars film.
    Returns:
        res (string) formatted string starting with film and followed by ordered list of characters

    """
    film_clean = clean_name(film)
    url = 'https://challenges.hackajob.co/swapi/api/films/?search=' + film_clean
    json_data = get_json(url)
    if len(json_data['results']) == 0:
        res = film + ': none'
    else:
        char_urls = json_data['results'][0]['characters']
        char_names = [get_json(x)['name'] for x in char_urls]
        char_names.sort()
        res = film + ': ' + ', '.join(char_names)
    return res


class Solution:
    def run(self, film, character):
        a = get_characters(film)
        b = get_films(character)
        return a + '; ' + b
