import requests

# Your API key (replace with your actual API key)
api_key = "b97ab04f11eccf48b5771bcfc25f4b18"
city = "Georgia"  # City name
url = f"http://api.openweathermap.org/data/2.5/weather?q=georgia&appid=b97ab04f11eccf48b5771bcfc25f4b18"

# Send GET request to OpenWeatherMap API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse the JSON response

    # Extract the weather description and temperature data
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius

    # Print the weather details
    print(f"Weather in {city}: {weather_description}")
    print(f"Temperature: {temperature:.2f}°C")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")
    print("Response message:", response.text)  # Display the response message for debugging
