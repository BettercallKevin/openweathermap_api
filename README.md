<h1>OPEN WEATHER MAP API OOP</h1>

<p>The goal of this repository is to offer classes with methods that will help user use the Open Weather Map api.</p>
<p>The open weather map is a weather service that provides weather data accessible through an api. The official website is https://openweathermap.org/.</p>

<h2>About the project</h2>

<p>This repository leverages the Python OOP to explore the Open Weather API data.</p>

<h3>Why using this repository</h3>

<p>Here are some reasons that may interest you in using this repository:</p>
<ul>
<li>You are building ETL/ELT using the openweathermap api,</li>
<li>You are building an application that uses the openweathermap api,</li>
<li>You are learning Python and search for a good example of OOP</li>
</ul>

<h3>What you will find in the repository</h3>

<p>This repository is composed of three main files:</p>
<ul>
<li>weather.py: which contains the classes</li>
<li>main.py: which contains examples of how to use functions</li>
<li>apikey.txt: the file in which you should write your apikey</li>
<li>requirements.txt: the packages you need to download to make this project work</li>
<li>webpage.html: an example of dataframe doable with the openweathermap api</li>
</ul>

<h3>Updates you should expect</h3>
<p>This is a project that requires many updates. Here are some elements that will be added to this repository:</p>
<ul>
<li>Unit testing</li>
<li>Forecast class</li>
<li>Additional testing</li>
</ul>

<h2>Getting started with OPEN WEATHER MAP API OOP</h2>

<p>In this section, you will find some guidance on how to use this repository efficiently. If you want more details about the open weather map api, I suggest you go directly to the website for further documentation: https://openweathermap.org/api.</p>

<h3>Cloning this repository</h3>

<p>You can clone this repository with the following command:</p>

```
git clone https://github.com/BettercallKevin/openweathermap_api.git
```

<h3>Requirements</h3>
<p>This project runs on python 3.11.3. The packages need to run this project will be found in the requirements.txt file.</p>

<p>I recommend you start by creating a virtual environment using this command:</p>

```
python -m venv env
source env/bin/activate
```
<p>Make sure you have pip installed. You can then download all the packages using the following command:</p>

```
pip install -r requirements.txt
```

<h3>Storing your API key</h3>
<p>You will need an API key in order to use the class methods. You will first need to your api key on the openweathermap website: https://home.openweathermap.org/api_keys.</p>
<p>Once you have your API key, you will need to copy it in a text file called apikey.txt. It is important that you respect the name of the file for methods to work.</p>

```
echo YOUR_API_KEY > apikey.txt
```

<h3>Using Classes</h3>

<p>In order to use the existing classes, you need to import them in your main document. In our case, we imported the Current package from weather.py</p>

```
from weather import Current
```

<h2>Key examples</h2>

<p>In this section, I will explore key examples to easily use to make the use of Open Weather Map API more efficient.</p>

<h3>Current weather object</h3>

<h4>Instantiating Current Weather Object </h4>
<p>This is the first ever step to make in order to use methods afterwards. We used the example of Paris, France.</p>

```
paris = Current(location="paris")
```

<p>Note that we need to add the "location=" in order to match the right argument with the string value "paris". There is no need to add capital letter at the beginning as the method will do it itself.</p>

<p>There are other ways you could instantiate a current weather object. You can precise a country code, or a country name.</p>

```
london = Current(location="london,UnitedKingdom")
rome = Current(location="rome,it"
```

<p>Make sure you always check the result because this is not a prefect method. For instance, "Rome, Italy" will send the weather information about Rome, US. </p>

<h4>Representation</h4>
<p>Representation is a subjective way to represent the object.</p>

```
print(paris)
```

<p>Terminal output:</p>

```
Weather information for Paris, FR:
2023, December 15, 10:30:26
The current temperature is 8.34C° though it feels like 7.71C°.
The minimum temperature is 7.34C°. Maximum will be 8.97C°.
Expect Clouds.
Sun will rise at 2023, December 15, 08:37:09 and will go down at 2023, December 15, 16:54:04.
```



<h4>Weather dictionary</h4>

<p>This method will show all key information about the weather.</p>

```
print(paris.weather_dictionary()
```

<p>Terminal output:</p>

```
{'city': 'Paris', 'country': 'FR', 'current_date': '2023, December 15, 11:35:13', 'weather_icon_url': 'https://openweathermap.org/img/wn/04d@2x.png', 'weather_general': 'Clouds', 'weather_details': 'overcast clouds', 'temperature': 8.79, 'feels_like': 8.23, 'minimum_temperature': 7.99, 'maximum_temperature': 9.58, 'pressure': 1036, 'humidity': 97, 'wind speed': 1.54, 'wind degree': 250, 'clouds': 100, 'rain_1h': 'test', 'snow_1h': 'test', 'sunrise': '2023, December 15, 08:37:09', 'sunset': '2023, December 15, 16:54:04'}

```

<p>The main difference with the original JSON is that there is no nested information and timestamp have been changed to human readable information. </p>

<h4>Empty Dataframe</h4>

<p>The particularity of this method is that it's a class method. It applies directly to the class and to no object. It creates an empty dataframe with columns for all the existing data in the data dictionary.</p>

```
df = Current.create_dataframe()
```

<h4>Object Dataframe</h4>
<p>To go faster on the building of your objects, there is built-in method that automatically creates a DataFrame for a given objects.</p>

```
paris = paris.weather_dataframe()
```
<h4>Value list</h4>
<p>Since the append() method is deprecated in recent Python version, you need to extract values directly from the dictionary of values. Use the value_list() method to do so. You can then add a row with this object values list into your empty class dataframe:</p>

```
df.loc['Paris'] = paris.value_list()
```