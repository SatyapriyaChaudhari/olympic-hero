# --------------
#Code starts here
best = data.loc[data['Country_Name'] == best_country, ['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
plt.bar(['Gold_Total','Silver_Total','Bronze_Total'], best.iloc[0])
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation = 45)
plt.show()


# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename({'Total' : 'Total_Medals'}, axis = 1, inplace = True)
print(data.head(10))


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', data['Better_Event'])
better_event = data['Better_Event'].value_counts().index[0]
print("Better Event with respect to all the performig countries is",better_event)


# --------------
#Code starts here
top_countries = pd.DataFrame(data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']],
                            columns = ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'])

top_countries.drop(top_countries.index[len(top_countries)-1], inplace = True)
print(top_countries.tail())

def top_ten (top_country, column_name):
    country_list = []
    #top_country.reset_index(drop = True, inplace = True)
    x = top_country.nlargest(10, column_name)
    country_list = list(x['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
print("Summer:\n",top_10_summer)

top_10_winter = top_ten(top_countries, 'Total_Winter')
print("Winter:\n",top_10_winter)

top_10 = top_ten(top_countries, 'Total_Medals')
print("Total:\n",top_10)

common = list(set(top_10_summer).intersection(top_10_winter).intersection(top_10))
print("Common:\n", common)


    


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.title('SUMMER')
plt.xticks(rotation = 45)
plt.show()

plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.title('WINTER')
plt.xticks(rotation = 45)
plt.show()

plt.bar(top_df['Country_Name'], top_df['Total_Summer'])
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.title('TOP 10')
plt.xticks(rotation = 45)
plt.show()


# --------------
#Code starts here

def country_gold(df, gr):
    country = df.loc[df['Golden_Ratio'] == gr, 'Country_Name'].iloc[0]
    #summer_country_gold = list(summer_df.loc[summer_df['Golden_Ratio']==summer_max_ratio, 'Country_Name'])
    return country

summer_df['Golden_Ratio'] = round(summer_df['Gold_Summer']/summer_df['Total_Summer'], 4)
summer_max_ratio = summer_df['Golden_Ratio'].max()
print("Maximum value of Golden Ratio in Summer: ",summer_max_ratio)
summer_country_gold = country_gold(summer_df, summer_max_ratio)
print("Country: ", summer_country_gold)

winter_df['Golden_Ratio'] = round(winter_df['Gold_Winter']/winter_df['Total_Winter'], 4)
winter_max_ratio = winter_df['Golden_Ratio'].max()
print("Maximum value of Golden Ratio in Winter: ",winter_max_ratio)
winter_country_gold = country_gold(winter_df, winter_max_ratio)
print("\nCountry: ", winter_country_gold)

top_df['Golden_Ratio'] = round(top_df['Gold_Total']/top_df['Total_Medals'], 4)
top_max_ratio = top_df['Golden_Ratio'].max()
print("Maximum value of Golden Ratio in Total: ",top_max_ratio)
top_country_gold = country_gold(top_df, top_max_ratio)
print("\nCountry: ", top_country_gold)



# --------------
#Code starts here
data_1 = data
data_1.drop(data_1.index[len(data_1)-1], inplace = True)
print(data_1.tail())
data_1['Total_Points'] = (3*data_1['Gold_Total']) + (2*data_1['Silver_Total']) + data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points']==most_points, 'Country_Name'].iloc[0]
print("Maximum Points: ", most_points)
print("Best Country: ", best_country)


