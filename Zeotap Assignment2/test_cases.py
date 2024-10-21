import unittest
from weather_fetcher import process_weather_data, convert_kelvin_to_celsius

class TestWeatherSystem(unittest.TestCase):

    def test_convert_kelvin_to_celsius(self):
        self.assertEqual(convert_kelvin_to_celsius(300), 26.85)

    def test_process_weather_data(self):
        mock_data = {
            'main': {'temp': 300},
            'weather': [{'main': 'Clear'}],
            'dt': 1609459200
        }
        result = process_weather_data(mock_data)
        self.assertEqual(result['temp_celsius'], 26.85)
        self.assertEqual(result['weather_condition'], 'Clear')

if __name__ == '__main__':
    unittest.main()
