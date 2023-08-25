# importing the requests library
import re
import requests
from bs4 import BeautifulSoup

# api-endpoint
URL = "https://flightplanning.navcanada.ca/cgi-bin/Fore-obs/metar.cgi"

def forecast(aerodrome, filename=None):
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {
        'NoSession': "",
        'Stations': aerodrome,
        'format': "raw",
        'Langue': "anglais",
        'Region': "can",
        'Location': "",
    }

    if filename is None:
        # sending get request and return the response as response object
        response = requests.get(url=URL, params=PARAMS)

        # parse the returned html, then combine the list into a single
        # block of text
        soup = BeautifulSoup(response.content, 'html.parser')

        for data in soup(['style', 'script']):
            data.decompose()

        content = ' '.join(soup.stripped_strings)

        # Remove anything that isn't actual METAR or TAF data
        content = content[content.find("METAR"):].split("Your", 1)[0]

    else:
        # get the data from a file instead
        with open(filename, 'r') as f:
            content = f.read()

    return content

if __name__ == "__main__":
    print(forecast("CYOW"))
