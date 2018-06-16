import urllib.parse
import urllib.request
import sys
import re
import datetime
import os
import errno
import xml.etree.ElementTree as ET
from WeatherData import *


# Iteratively collect each aerodrome acronym from Aerodromes.xml, then generate
# an appropriate filename for the data collected for said aerodrome based on
# the date and time that the data is obtained. Next, create a subfolder inside
# the parent path metardata. Finally, collect the intended data with getMETAR(),
# and put the data into the new file created.
def gather_and_write(dromes_list="Aerodromes.xml"):

	# Use xml.etree to parse the XML file the aerodrome data is kept in
    doc = ET.parse(dromes_list)

	# Identify the root level of the XML tree
    root = doc.getroot()

	# Iterate through the children, which correspond to the aerodromes
    for child in root:
	# Get the aerodrome's abbreviation
        dromeID = child[0].text
        weather_collector = WeatherCollector(dromeID)
        weather_collector.gather_data()
        print(weather_collector.get_dromeID())

        weather_writer = WeatherWriter(dromeID, "../weather", weather_collector)
        weather_writer.write_metar(weather_collector.get_metar())
        weather_writer.write_taf(weather_collector.get_taf())

if __name__ == "__main__":
    gather_and_write()
