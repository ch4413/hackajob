import urllib.request
import json


def get_json(url_string):
    """
    Returns dictionary of json data from URL

    Args:
    	url_string (string) valid string of URL site containing JSON
    Returns:
    	data (dict) dictionary of retrived JSON
    """
    with urllib.request.urlopen(url_string) as url:
        data = json.loads(url.read().decode())
    return data


def count_goals(data, teamKey):
    """
    counts goals in dictionary of fixtures for given teamKey

    Args:
    	data (dict) dictionary of season's football results
    	teamKey (string) string of valid key within JSON for team
    returns:
    	int for goals if valid teamKey, string message if not found.
    """
    goals = 0
    key_found = False
    for i in range(len(data['rounds'])):
        for j in range(len(data['rounds'][i]['matches'])):
            if data['rounds'][i]['matches'][j]['team1']['key'] == teamKey:
                goals += data['rounds'][i]['matches'][j]['score1']
                key_found = True
            elif data['rounds'][i]['matches'][j]['team2']['key'] == teamKey:
                goals += data['rounds'][i]['matches'][j]['score2']
                key_found = True
    if key_found:
        return goals
    else:
        return 'Key "{0}" not found'.format(teamKey)


class Solution:

    def run(self, teamKey):
        """
        Runs pipeline to retrieve data and count gols for given teamKey

        Args:
            teamKey (string) string of team key in data
        Returns:
            goals (int) count of goals, both home and away
        """
        data = get_json("https://raw.githubusercontent.com/openfootball/football.json/master/2014-15/en.1.json")
        goals = count_goals(data, teamKey)

        return goals

