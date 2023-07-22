#Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the current weather forecast.
#Leverage OpenWeatherMap API to fetch weather data and parse it using Python.
#Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.
#Solution:
import requests
import datetime

# Function to retrieve weather data from OpenWeatherMap API
def get_weather_data(city_name, units):
    API_KEY = "a73f1df852b1f6c1d2c74f2482fb348d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_param = "+".join(city_name)

    standard_units_param = ""
    metric_units_param = "metric"
    imperial_units_param = "imperial"

    standard_units = {
        "temperature": "K",
        "pressure": "hPa",
        "humidity": "%"
    }

    metric_units = {
        "temperature": "°C",
        "pressure": "hPa",
        "humidity": "%"
    }

    imperial_units = {
        "temperature": "°F",
        "pressure": "hPa",
        "humidity": "%"
    }

    units_mapping = {
        "1": (standard_units_param, standard_units, "Standard"),
        "2": (metric_units_param, metric_units, "Metric"),
        "3": (imperial_units_param, imperial_units, "Imperial")
    }

    units_param, units_labels, units_name = units_mapping.get(units, (standard_units_param, standard_units, "Standard"))

    url = f"{base_url}appid={API_KEY}"
    if units_param:
        url += f"&units={units_param}"
    url += f"&q={city_param}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        date = data["dt"]
        name = data["name"]
        temperature = data["main"]["temp"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        humidity = data["main"]["humidity"]
        sunrise = data["sys"]["sunrise"]
        sunset = data["sys"]["sunset"]
        description = data["weather"][0]["description"]
        rain1h = data.get("rain", {}).get("1h", 0)
        rain3h = data.get("rain", {}).get("3h", 0)
        snow1h = data.get("snow", {}).get("1h", 0)
        snow3h = data.get("snow", {}).get("3h", 0)
        clouds = data["clouds"]["all"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        wind_gust = data.get("wind", {}).get("gust", 0)
        

        return {
            "date": date,
            "name": name,
            "temperature": temperature,
            "temp_min": temp_min,
            "temp_max": temp_max,
            "humidity": humidity,
            "sunrise": sunrise,
            "sunset": sunset,
            "description": description,
            "rain1h": rain1h,
            "rain3h": rain3h,
            "snow1h": snow1h,
            "snow3h": snow3h,
            "clouds": clouds,
            "pressure": pressure,
            "wind_speed": wind_speed,
            "wind_gust": wind_gust,
            "units_labels": units_labels,
            "units_name": units_name
        }
    except requests.exceptions.HTTPError:
        print("\nCity not found.")
        return None

# Main function to interact with the user
def main():
    # Get the city name from the user
    city_name = input("Enter city name: ").split()
    # Retrieve weather data using standard units of measurement
    data = get_weather_data(city_name, "1")

    if data:
        units_labels = data["units_labels"]
        units_name = data["units_name"]

        # Display weather information in standard units
        print(f"\nWeather forecast in {units_name} units of measurement for {' '.join(city_name)}:")
        print(f"Date: {datetime.datetime.utcfromtimestamp(data['date']).strftime('%Y-%m-%d %H:%M:%S')} UTC")
        print(f"City: {data['name']}")

        print(f"\nTemperature: {data['temperature']} {units_labels['temperature']}", end="\t")
        print(f"\tWeather Desc: {data['description']}", end="\t")
        print(f"\tHumidity: {data['humidity']} {units_labels['humidity']}", end="\t")
        print(f"\tRain (last hour): {data['rain1h']} mm", end="\t")
        print(f"\tSnow (last hour): {data['snow1h']} mm")

        print(f"Minimum_Temp: {data['temp_min']} {units_labels['temperature']}", end="\t")
        print(f"\tSunrise: {datetime.datetime.utcfromtimestamp(data['sunrise'])}", end="\t")
        print(f"\tPressure: {data['pressure']} {units_labels['pressure']}", end="\t")
        print(f"\tRain (last 3 hours): {data['rain3h']} mm", end="\t")
        print(f"\tWind Speed: {data['wind_speed']} m/s")

        print(f"Maximum_Temp: {data['temp_max']} {units_labels['temperature']}", end="\t")       
        print(f"\tSunset: {datetime.datetime.utcfromtimestamp(data['sunrise'])}", end="\t")
        print(f"\tCloudiness: {data['clouds']} %", end="\t")
        print(f"\tSnow (last 3 hours): {data['snow3h']} mm", end="\t")
        print(f"\tWind Gust: {data['wind_gust']} m/s\n")

        # Display weather information in standard, metric, and imperial units
        units_prompt = "Choose your preferred Units of measurement:\n" \
                       "Press 1 for Standard\n" \
                       "Press 2 for Metric\n" \
                       "Press 3 for Imperial\n" \
                       "Press Enter to exit\n"

        units = input(units_prompt)

        while units:
            # Retrieve weather data using the selected units of measurement
            data = get_weather_data(city_name, units)

            if data:
                units_labels = data["units_labels"]
                units_name = data["units_name"]
                
                # Display weather information in selected units
                print(f"\nWeather forecast in {units_name} units of measurement for {' '.join(city_name)}:")
                print(f"Date: {datetime.datetime.utcfromtimestamp(data['date']).strftime('%Y-%m-%d %H:%M:%S')} UTC")
                print(f"City: {data['name']}")

                print(f"\nTemperature: {data['temperature']} {units_labels['temperature']}", end="\t")
                print(f"\tWeather Desc: {data['description']}", end="\t")
                print(f"\tHumidity: {data['humidity']} {units_labels['humidity']}", end="\t")
                print(f"\tRain (last hour): {data['rain1h']} mm", end="\t")
                print(f"\tSnow (last hour): {data['snow1h']} mm")

                print(f"Minimum_Temp: {data['temp_min']} {units_labels['temperature']}", end="\t")
                print(f"\tSunrise: {datetime.datetime.utcfromtimestamp(data['sunrise'])}", end="\t")
                print(f"\tPressure: {data['pressure']} {units_labels['pressure']}", end="\t")
                print(f"\tRain (last 3 hours): {data['rain3h']} mm", end="\t")
                print(f"\tWind Speed: {data['wind_speed']} m/s")

                print(f"Maximum_Temp: {data['temp_max']} {units_labels['temperature']}", end="\t")       
                print(f"\tSunset: {datetime.datetime.utcfromtimestamp(data['sunrise'])}", end="\t")
                print(f"\tCloudiness: {data['clouds']} %", end="\t")
                print(f"\tSnow (last 3 hours): {data['snow3h']} mm", end="\t")
                print(f"\tWind Gust: {data['wind_gust']} m/s\n")
            else:
                print("\nOpenWeatherMap does not have weather information for the given city")

            units = input(units_prompt)

if __name__ == "__main__":
    main()
