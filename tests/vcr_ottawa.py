import unittest
import vcr
import sys
from vane import *


class TestVaneBasic(unittest.TestCase):
    def setUp(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/synopsis.yaml'):
            self.test_vane_ottawa = weathervane.WeatherCollector("CYOW")
            self.test_vane_ottawa.gather_weather_data()

    def test_ottawa_aerodrome(self):
        self.assertGreater(len(self.test_vane_ottawa.parsed_data), 0)
        self.assertIn("CYOW", self.test_vane_ottawa.parsed_data)
        self.assertNotIn("CYUL", self.test_vane_ottawa.parsed_data)

if __name__ == '__main__':
    unittest.main()
