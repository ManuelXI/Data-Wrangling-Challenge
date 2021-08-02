import pandas as pd

# Reading Wiki Article
df = pd.read_html('https://en.wikipedia.org/wiki/Road_safety_in_Europe')
# print(df[2])
# df[2].to_csv('data.csv')
# Importing Required Table
df[2].to_csv('data.csv', index=False)


df = pd.read_csv('data.csv')
# Dropping Unrequired Columns
df = df.drop(columns=['Road Network Length (in km) in 2013[29]',
             'Number of People Killed per Billion km[30]', 'Number of Seriously Injured in 2017/2018[30]'])
df.sort_values('Road deaths per Million Inhabitants in 2018[30]')
# Inserting Year Columns
df.insert(1, 'Year', 2018)

# Renaming Columns
new_col = ['Country', 'Year', 'Area (thousands of km2)',
           'Population in 2018', 'GDP per capita in 2018',
           'Population density (inhabitants per km2) in 2017',
           'Vehicle ownership (per thousand inhabitants) in 2016',
           'Total Road Deaths in 2018',
           'Road deaths per Million Inhabitants in 2018']
df.columns = new_col

# Writing Final Table to CSV File
df.to_csv('data.csv', index=False)
