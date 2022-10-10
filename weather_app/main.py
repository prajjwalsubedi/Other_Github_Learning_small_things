# data = []
#
# with open("weather_data.csv") as weather_data:
#     lines = weather_data.readline()
#     for line in lines:
#         data.append(line.strip())
#
# print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(temperatures)


# import pandas
# data = pandas.read_csv("weather_data.csv")
#
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # print(data["temp"].max())
#
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

import pandas

data = pandas.read_csv("squirrel_data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Red"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Red", "Black"],
    "count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("color count of squirrel.csv")
