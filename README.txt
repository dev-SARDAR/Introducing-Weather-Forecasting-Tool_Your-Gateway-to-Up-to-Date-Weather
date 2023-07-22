# Weather_Forecasting_Tool_SARDAR_MAHBOOB
Weather Forecasting Tool - Created a command line tool that accepts a city's name and returns the current weather forecast. It Leverages OpenWeatherMap API to fetch weather data and parse it using Python.  
The file consists of the get_weather_data() function that is used to call the OpenWeatherMap Api which takes in city_name as an argument from the command line and generates a url consisting of api key,city_name and the official OpenWeatherMap url.
The current weather forecast is requested by calling the request method with takes in above generated url to get back all required information.
The main() method takes the user input as city_name and prints the current weather forecast by calling the  get_weather_data() method.
The try and catch block helps in handling city not found error and returns back the console so that flow of instructions is not disturbed.
The results can be generated in standard units of measurement, metric units of measurement or imperial units of measurement. 
The user will be prompted when entering the name of the city in the main() method to mention the type of units of measurement that the user would like to see the final output being presented  on the treminal.
There has been extensive use of Github Copilot when designing the code for weather forecasting tool where all the required libraries which were being used were prompted and with help of timely comments the code was being optimised according to our needs.

Demo Video: https://drive.google.com/file/d/1UD1dYeTq2ytkThJKyJO4_a2Uek1w97gu/view
