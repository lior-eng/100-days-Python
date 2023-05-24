# Challenge

# with open('./Day-25/weather_data.csv') as data:
#     weather_data = data.readlines()
# print(weather_data)

# Challenge

# import csv

# with open('./Day-25/weather_data.csv',mode= 'r') as data:
#     weather_data = csv.reader(data)
#     temperatures = []
#     next(weather_data)
#     for row in weather_data:
#         temperatures.append(int(row[1]))
#     print(temperatures)