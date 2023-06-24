# Weather_Forecasting_Tool
Weather Forecasting Tool - Created a command line tool that accepts a city's name and returns the current weather forecast. It Leverages OpenWeatherMap API to fetch weather data and parse it using Python.  
The file consists of the get_weather_data() function that is used to call the OpenWeatherMap Api which takes in city_name as an argument from the command line and generates a url consisting of api key,city_name and the official OpenWeatherMap url.
The current weather forecast is requested by calling the request method with takes in above generated url to get back all required information.
The main() method takes the user input as city_name and prints the current weather forecast by calling the  get_weather_data() method.
The try and catch block helps in handling city not found error and returns back the console so that flow of instructions is not disturbed.
