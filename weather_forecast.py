import requests
from datetime import date, timedelta

start_date = date.today() + timedelta(days=1)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 50.073658,
    "longitude": 14.418540,
    "start_date": start_date,
    "end_date": start_date,
    # "forecast_days": 1,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_mean"
}

response = requests.get(url, params=params).json()

# for weather_parameter in response:
#     print(weather_parameter)
#     print(response[weather_parameter])

next_day = response['daily']['time'][0]
max_temperature = response['daily']['temperature_2m_max'][0]
min_temperature = response['daily']['temperature_2m_min'][0]
precipitation_probability_mean = response['daily']['precipitation_probability_mean'][0]
celcius_symbol = response['daily_units']['temperature_2m_max']
precipitation_symbol = response['daily_units']['precipitation_probability_mean']

print(f'Your weather forecast for {next_day}:\n'
      f'Minimum temperature: {min_temperature}{celcius_symbol}\n'
      f'Maximum temperature: {max_temperature}{celcius_symbol}\n'
      f'Precipitation probability: {precipitation_probability_mean}{precipitation_symbol}'
      )
