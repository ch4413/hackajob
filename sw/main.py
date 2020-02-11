import urllib.request
import json


def get_json(url_string):
    """
    """
    with urllib.request.urlopen(url_string) as url:
        data = json.loads(url.read().decode())
    return data


def clean_name(name):
    """

    """
    return name.replace(' ', '%20')


class Solution:

    def run(self, character):
        """

        """
        name = clean_name(character)
        url = 'https://challenges.hackajob.co/swapi/api/people/?search=' + name
        json_data = get_json(url)
        numberOfFilms = len(json_data['results'][0]['films'])
        return numberOfFilms
