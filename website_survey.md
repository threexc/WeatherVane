# Survey of METAR/TAF/Other Observation Data Sources

## Introduction

The WeatherVane project's primary objective is to track trends and
accuracy not only in aviation forecasts, but also in climate and extreme
weather frequency over various regions and temporal intervals.
Therefore, it is critical that a sizeable archive of reference data
spanning years (if not decades) and with a high resolution (i.e.
incorporating independent measurements from as many weather stations
and/or aerodromes as possible) is available for comparison against
current observations (e.g. METAR), forecasts (e.g. TAF), and any other
secondary meteorological data that may be useful in providing meaningful
and actionable results.

## Comparison of Sources

|                         | Range    | METAR (days) | TAF (days) | SIGMET  | FB  | URL | Notes |
| ---                     | ---      | ---          | ---        | ---     | --- | --- | ---   |
| Aviation Weather Center | USA      | 120          | Current    | Yes     | Yes | https://www.aviationweather.gov/ | Useful info, limited history, appears mostly US-centric|
| NAV Canada              | Canada   | Current      | Current    | Yes     | Yes | https://flightplanning.navcanada.ca/cgi-bin/CreePage.pl?Langue=anglais&NoSession=&Page=forecast-observation&TypeDoc=html | Canada-centric, limited history |
| OGIMET                  | World    | 6000+        | 6000+      | Unknown | Yes | https://www.ogimet.com/home.phtml.en | Oldest records found (2004-2005) |
| metar-taf.com           | World    | 5800+        | 5800+      | Unknown | No  | https://metar-taf.com/ | Second oldest records, but requires financial contribution |

Programatically, OGIMET is probably the best option simply because of
its visible query encoding in the URL, and data archive that is much
larger than the others. Ideally, OGIMET data could be compared against
metar-taf.com or a similar database with extensive history. 
