import requests

API_KEY = 'your_api_key'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(data):
    temp_k = data['main']['temp']
    temp_c = convert_kelvin_to_celsius(temp_k)
    weather_condition = data['weather'][0]['main']
    return {
        'temp_celsius': temp_c,
        'weather_condition': weather_condition,
        'time': data['dt']
    }

def main():
    for city in CITIES:
        weather_data = get_weather_data(city)
        processed_data = process_weather_data(weather_data)
        print(f"{city}: {processed_data['temp_celsius']}°C, {processed_data['weather_condition']}")

if __name__ == "__main__":
    main()
