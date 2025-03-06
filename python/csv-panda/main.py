import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
colors = data['Primary Fur Color'].value_counts().reset_index()
colors.columns = ['Color', 'Count']
colors.to_csv('squirrel_colors.csv')