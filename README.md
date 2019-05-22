# WeatherVane

WeatherVane is a project designed to chronicle the changing weather patterns across Canada in the face of climate change, as well analyze the way we forecast the weather from city to city. It currently relies on the publicly-available information located on the NAV CANADA [website](https://flightplanning.navcanada.ca/cgi-bin/CreePage.pl?Langue=anglais&NoSession=NS_Inconnu&Page=Fore-obs%2Fmetar-taf-map&TypeDoc=html), and no claims are made to the data itself or the methods by which it is obtained.

WeatherVane is designed to be split into two parts:

1. WeatherCollector/WeatherWriter - A tool for periodically collecting and archiving the METAR (Aviation Routine Weather Report) and TAF (Terminal Aerodrome Forecast), which is mostly already complete (with room for improvements)
2. WeatherAnalyzer - A tool to analyze the trends inherent in the data, and provide conditional probabilities for conditions on future forecasts given a user-specified time of day/year


As the project is still under development, things are likely to change significantly, and WeatherAnalyzer does not exist in the repo yet. Currently, best practice for setting up the former two tools is to configure a cronjob to run the gather_and_write.py file.

Longer-term goals for the project:

1. Insertion of the data into a time series database - possibly using InfluxDB
2. Full unit testing and Jenkins and/or Travis CI support
3. A nice webpage displaying key/sufficient statistics

If you can lend some suggestions or know of an existing database of historical **forecasts** (not just historical weather conditions), please contact me at tvgamblin@gmail.com.
