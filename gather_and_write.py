#!/usr/bin/python3

import urllib.parse
import urllib.request
import sys
import re
import datetime
import os
import errno
import xml.etree.ElementTree as ET
from vane import weathervane

def get_aerodrome(dromeID):
    vane = weathervane.WeatherCollector(dromeID)
    vane.gather_weather_data()
    print(vane.get_dromeID())

    logger = weathervane.WeatherWriter(dromeID, "../weather", vane)
    logger.write_metar(vane.metar)
    logger.write_taf(vane.taf)

def gather_and_write(dromes_list="Aerodromes.xml"):
    directory = os.path.dirname(os.path.realpath(__file__))
	# Use xml.etree to parse the XML file the aerodrome data is kept in
    doc = ET.parse(directory + "/" + dromes_list)

	# Identify the root level of the XML tree
    root = doc.getroot()

	# Iterate through the children, which correspond to the aerodromes
    for child in root:
	# Get the aerodrome's abbreviation
        dromeID = child[0].text
        get_aerodrome(dromeID)

if __name__ == "__main__":
    gather_and_write()
