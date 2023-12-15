import pandas as pd
from datetime import datetime
import requests
import json
import string
from PIL import Image
from io import BytesIO
import pandas as pd


# Make sure you add your API key within the
with open ("apikey.txt", "r") as file:
    apikey = file.read()

class Weather:
    def __init__(self, apikey = apikey, location = "Paris", unit = "metric", url ="https://api.openweathermap.org/data/2.5/"):
        self.apikey = apikey
        self.location = string.capwords(location)
        self.unit = unit
        self.url = url

###### Current Weather
"""
This class is meant to render the weather for an 
"""
class Current(Weather):
    def __init__(self, type = "weather?", **kwargs):
        super().__init__(**kwargs)
        self.type = type
        self.full_url = self.url + self.type + "q=" + self.location + "&units=" + self.unit + "&appid=" + self.apikey
        self.result = requests.get(self.full_url).json()

    # The JSON format is where all the information from the API call will appear.
    def current_json(self):
        '''
        This function returns the json format of current weather result attribute.
        :return: json all the information from the requests of the full url.
        '''
        return self.result

    def temperature(self):
        '''
        The temperature method returns all the information nested in the temperature key of the full json from the url request.
        :return: json with 'temp', 'feels_like', 'temp min', 'temp_max', 'pressure', 'humidity'.
        '''
        temperature = self.current_json()['main']
        return temperature

    def weather_info(self):
        '''
        The weather_info method returns the 'weather' nested information.
        :return: list with 'id', 'visibility', 'description', 'icon'
        '''
        weather = self.current_json()['weather']
        return weather

    def coordinate(self):
        '''
        The coordinate method returns the "coord" nested information.
        :return: json with 'lon' and 'lat' coordinates
        '''
        coordinate = self.current_json()['coord']
        return coordinate

    def visibility(self):
        '''
        The visibility method returns the visibility in meters
        :return: int: the visibility in meters
        '''
        visibility = self.current_json()['visibility']
        return visibility

    def wind(self):
        '''
        The wind method returns the 'wind' nested information
        :return: json: with 'speed' (str, meter per second) and 'deg' (degrees)
        '''
        wind = self.current_json()['wind']
        return wind

    def cloud(self):
        '''
        The cloud method returns the clouds level.
        :return: json: all in percentage.
        '''
        cloud = self.current_json()['clouds']
        return cloud

    def date_timestamp(self):
        '''
        The date methods extracts the date from the JSON return
        :return: timestamp date in format timestamp
        '''
        date = self.current_json()['dt']
        return date

    def general_info(self):
        '''
        This method returns all other information about the weather in the JSON response
        :return: json includes "type", "id", "country", "sunrise", "sunset"
        '''
        general = self.current_json()['sys']
        return general

    def timezone(self):
        '''
        The timezone method returns the timezone in which the selected location is. The timezone for weather api respects the GMT format.
        For instance, timezone for London, UK, would be 0 since it's UTC.
        :return: int: timezone
        '''
        timezone = self.current_json()['timezone']
        return timezone

    def id_number(self):
        '''
        The id_number method returns the id number given in the JSON response.
        :return: int: id
        '''
        id_number = self.current_json()['id']
        return id_number

    def city_name(self):
        '''
        This method returns the name of the city in the JSON response.
        :return: str: city name
        '''
        city_name = self.current_json()['name']
        return city_name

    def cod(self):
        '''
        This method returs the internal code provided in the JSON response.
        This code is part of the structure to understand the weather.
        :return: int: code
        '''
        cod = self.current_json()['cod']

    def rain_1h(self):
        '''
        This method returns the rain nested information if it can apply to the situation.
        According to the openweathermap api, this might not be appearing if there is no rain.
        :return: JSON: with rain information including:
        '''
        try:
            rain_1h = self.current_json()['rain']['1h']
            return rain_1h

        except Exception as e:
            return "No rain"

    def snow_1h(self):
        '''
        This method returns the snow nested information if it can apply to the situation.
        According to the openweathermap api, this might not be appearing if there is no snow.
        :return: JSON: snow information
        '''
        try:
            rain_1h = self.current_json()['snow']['1h']
            return rain_1h

        except Exception as e:
            return "No snow"

    def current_date(self):
        '''
        The current_date method converts the "dt" key from the JSON into a readable time for human.
        It leverages the datetime packages to transform a timestamp into a datetime object
        :return: date: the date of recording
        '''
        current_date = datetime.utcfromtimestamp(self.date_timestamp() + self.timezone()).strftime("%Y, %B %d, %H:%M:%S")
        return current_date

    def sunrise_time(self):
        '''
        The current method converts the sunrise time from the JSON into a readable time for human.
        It leverages the datetime packages to transform a timestamp into a datetime object
        :return: date: exact time of sunrise
        '''
        sunrise = datetime.utcfromtimestamp(self.general_info()['sunrise'] + self.timezone()).strftime("%Y, %B %d, %H:%M:%S")
        return sunrise

    def sunset_time(self):
        '''
        The current method converts the sunset time from the JSON into a readable time for human.
        It leverages the datetime packages to transform a timestamp into a datetime object
        :return: date: exact time of sunrise
        '''
        sunset = datetime.utcfromtimestamp(self.general_info()['sunset'] + self.timezone()).strftime("%Y, %B %d, %H:%M:%S")
        return sunset

    def to_datetime(self, timestamp, timezone):
        '''
        This method takes a timestamp and converts it into a datetime object.
        :param timestamp:
        :return: datetime
        '''
        date_time = datetime.utcfromtimestamp(timestamp + timezone).strftime("%Y, %B %d, %H:%M:%S")
        return date_time

    # Complex data to add
    def weather_icon_url(self):
        '''
        The weather_icon_url method uses the icon code to create the full url that gives access to the icon
        :return: url
        '''
        base = "https://openweathermap.org/img/wn/"
        extension = "@2x.png"
        icon_code = self.weather_info()[0]['icon']
        url = base + icon_code + extension
        return url

    def weather_icon(self):
        '''
        The weather_icon method returns the corresponding icon to the current weather.
        :return: icon information
        '''
        response = requests.get(self.weather_icon_url())

        # Check if the request was successful
        if response.status_code == 200:
            # Open the image from the bytes in the response
            image = Image.open(BytesIO(response.content))

            # Display the image
            return image
        else:
            print(f"Failed to retrieve the image. Status code: {response.status_code}")

    # Dictionary methods to store all the data
    def weather_dictionary(self):
        '''
        This method returns a dictionary with all key information
        :return: dict all weather information organised in a dictionary
        '''
        all_info = {
            "city": self.city_name(),
            "country": self.general_info()['country'],
            "current_date": self.current_date(),
            "weather_icon_url": self.weather_icon_url(),
            "weather_general": self.weather_info()[0]['main'],
            "weather_details": self.weather_info()[0]['description'],
            "temperature": self.temperature()['temp'],
            "feels_like": self.temperature()['feels_like'],
            "minimum_temperature": self.temperature()['temp_min'],
            "maximum_temperature": self.temperature()['temp_max'],
            "pressure": self.temperature()['pressure'],
            "humidity": self.temperature()['humidity'],
            "wind speed": self.wind()['speed'],
            "wind degree": self.wind()['deg'],
            "clouds": self.cloud()['all'],
            "rain_1h": self.rain_1h(),
            "snow_1h": self.snow_1h(),
            "sunrise": self.sunrise_time(),
            "sunset": self.sunset_time()
        }
        return all_info

    def value_list(self):
        '''
        This method returns all the values from the dictionary of weather. This method is used to create dataframes.
        :return: list: the list of all values in the weather dictionary.
        '''
        value_list = [value for value in self.weather_dictionary().values()]
        return value_list

    # Pandas dataframe methods
    def weather_dataframe(self):
        '''
        This method will create a dataframe with the data provided in the dictionary of weather.
        :return: dictionary of weather.
        '''
        transformed_list = [self.weather_dictionary()]
        df = pd.DataFrame(transformed_list)
        return df

    @classmethod
    def create_dataframe(cls):
        '''
        This method creates an empty dataframe that contains the all the different keys of the weather dictionary.
        :return: Dataframe : empty dataframe with all set columns.
        '''
        df = pd.DataFrame(columns=["city", "country", "current_date", "weather_icon_url", "weather_general", "weather_details", "current_temp", "feels_like_temp", "temp_min", "temp_max", "pressure", "humidity", "wind_speed", "wind_degree", "cloud", "rain_1h", "snow_1h", "sunrise", "sunset"])
        return df

    def __repr__(self):
        return (f"Weather information for {self.weather_dictionary()['city']}, {self.weather_dictionary()['country']}:\n"
                f"{self.weather_dictionary()['current_date']}\n"
                f"The current temperature is {self.weather_dictionary()['temperature']}C° though it feels like {self.weather_dictionary()['feels_like']}C°.\n"
                f"The minimum temperature is {self.weather_dictionary()['minimum_temperature']}C°. Maximum will be {self.weather_dictionary()['maximum_temperature']}C°.\n"
                f"Expect {self.weather_dictionary()['weather_general']}.\n"
                f"Sun will rise at {self.weather_dictionary()['sunrise']} and will go down at {self.weather_dictionary()['sunset']}.\n")
