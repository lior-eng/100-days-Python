import pandas as pd

data = pd.read_csv('./Day-25/weather_data.csv')

data_dict = data.to_dict()
temperatures_list = data["temp"].to_list()
temperatures_mean = data["temp"].mean()
max_temperature = data["temp"].max()

day_with_max_temperature = data[data.temp == max_temperature]

Monday_data = data[data.day == "Monday"]
Monday_temp_in_Faherenheit = float(Monday_data.temp * 1.8 + 32)

#########################  Challenge   #########################

central_park_squirrel_data = pd.read_csv('./Day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
squirrel_count_series = central_park_squirrel_data["Primary Fur Color"].value_counts()
squirrel_count_dataframe = pd.DataFrame(squirrel_count_series)
squirrel_count_csv = squirrel_count_dataframe.to_csv("./Day-25/squirrel_count.csv")