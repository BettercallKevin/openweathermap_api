from weather import Current
from IPython.core.display import HTML


####### individual dataframe

# We will instantiate the weather for Paris
paris = Current(location="Paris")

# Other examples of instantiation using city and country
rome = Current(location="Rome,it")
london = Current(location="london,UnitedKingdom")

# Explore the representation of the object
#print(paris)
#print(rome)
#print(london)

# Information dictionary
dict_paris = paris.weather_dictionary()

print(dict_paris)
# We create an empty dataframe using a class method
df = Current.create_dataframe()

# We create our dataframe for Paris weather
df_paris = paris.weather_dataframe()

#print(df_paris)

# We can add a new row to our dataframe with the information of paris
df.loc['Paris'] = paris.value_list()

####### Rendering in HTML our dataframe
"""
We want to make sure we can create a dataframe that also shows the icon given through the link.
"""

# Converting links to html tags
# I found this piece of code from a medium article: https://towardsdatascience.com/rendering-images-inside-a-pandas-dataframe-3631a4883f60
def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'
# Rendering the dataframe as HTML table
df.to_html(escape=False, formatters=dict(weather_icon_url=path_to_image_html))
# Rendering the images in the dataframe using the HTML method.
HTML(df.to_html(escape=False,formatters=dict(weather_icon_url=path_to_image_html)))
# Saving the dataframe as a webpage
df.to_html('webpage.html',escape=False, formatters=dict(weather_icon_url=path_to_image_html))