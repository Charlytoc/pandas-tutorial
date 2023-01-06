# print('Hello World')
import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')

# print(data_frame)
# ages = [23,45,7,34,6,63,36,78,54,34]
# data = pd.Series(ages)
# print(data)
# data = pd.date_range('05-01-2021', '05-12-2021')
# print(data)

# my_series = pd.Series([2, 4, 6, 8, 10])
# def divideByTwo(x):
#     return (x/2)


# print(my_series.apply(divideByTwo))
# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]
# df = pd.DataFrame(data,columns=['Brand','Model', 'Color'])
# print(df)

# data = [
#     { 
#         "brand": "Toyota", 
#         "make": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford", 
#         "make": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porche", 
#         "make": "Cayenne",
#         "color": "White"
#     },
#     {
#         "brand": "Tesla", 
#         "make": "Model S",
#         "color": "Red"
#     }
# ]
# df = pd.DataFrame(data)
# print(df)
# data = pd.read_csv('.learn/assets/pokemon_data.csv')

# # print(data.tail(n=3))
# print(len(data.loc[data['Legendary'] == True]))

df = pd.read_csv('./.learn/assets/us_baby_names_right.csv')
# print(df.head())
df = df.drop(columns='Unnamed: 0')
# print(df['Gender'].value_counts())
grouped_df = df.groupby('Name')

print(len(grouped_df.sum()))