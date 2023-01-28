# Works Cited
# code adapted from
# https://rapidapi.com/api-sports/api/api-football


import requests
import json


def get_info(return_query, parameter):
    url = "https://api-football-v1.p.rapidapi.com/v3/" + parameter

    querystring = return_query

    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.text
    json_data = json.loads(response)
    return json_data
