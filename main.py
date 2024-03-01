#imports
import requests
import json

api_key = '0ce5a398e21ada8cce7ff148c506199b'


# The base URL for the OpenWeather API
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

# The city you want to get the weather for
city_name = 'Boston'

# Construct the URL with the city name and API key
url = base_url + f'q={city_name}&appid={api_key}'

# Send a GET request to the OpenWeather API
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Convert temperature from Kelvin to Fahrenheit
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Extract temperature in Kelvin from the response
temperature_kelvin = data['main']['temp']

# Convert temperature to Fahrenheit
temperature_fahrenheit = kelvin_to_fahrenheit(temperature_kelvin)

# Check if the request was successful
if response.status_code == 200:
    # Extract relevant weather information
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']

    # Print the weather information
    # Print the temperature in Fahrenheit
    print(f'Temperature: {temperature_fahrenheit}°F')
    print(f'Humidity: {humidity}%')
    print(f'Weather Description: {weather_description}')

    # Save the response in JSON format
    with open('weather_response.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print('Weather response saved successfully.')
else:
    # Print an error message if the request was not successful
    print(f'Error: {data["message"]}')