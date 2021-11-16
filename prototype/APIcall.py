from requests import Request, Session 
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import config


def getQuotes(slug):
    APIkey = config.APIkey


    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': APIkey 
    }      


    parameters = {
            'slug' : slug
    }

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)



getQuotes("dogecoin")