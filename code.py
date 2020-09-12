# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)


data.rename(columns={'Total':'Total_Medals'},inplace =True)
print(data.head(10))



# --------------
#Code starts here

data["Better_Event"] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer','Winter')

data['Better_Event'] =np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event']) 

print(data.head(10))

better_event = data.Better_Event.value_counts().idxmax()
print(better_event)




# --------------
#Code starts here

# A new dataframe subset called 'top_countries' with the columns
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']] 

# Dropping the last row as it contains Total values.
top_countries.drop(146,axis=0,inplace=True)


top_10_summer = list(top_countries.nlargest(10,'Total_Summer')['Country_Name'])
top_10_winter = list(top_countries.nlargest(10,'Total_Winter')['Country_Name'])
top_10 = list(top_countries.nlargest(10,'Total_Medals')['Country_Name'])


def common_member(top_10_summer, top_10_winter, top_10): 
    a = set(top_10_summer) 
    b = set(top_10_winter) 
    c = set(top_10)
    if (a & b & c): 
        common = (a & b & c)
    return common


common =list(common_member(top_10_summer, top_10_winter, top_10))
print(common)


# --------------
#Code starts here

(top_10_summer, top_10_winter, top_10)

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]


summer_df.plot(kind='bar', x='Country_Name', y='Total_Summer', figsize = (10, 7))
winter_df.plot(kind='bar', x='Country_Name', y='Total_Winter', figsize = (10, 7))
top_df.plot(kind='bar', x='Country_Name', y='Total_Medals', figsize = (10, 7))
# print(summer_df)


# --------------
#Code starts here

#finding the ratio of Gold medal in Summer wrt total summer
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
# Finding the country with the max value using Loc
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']


#finding the ratio of gold medal in Winter wrt total Winter
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
# Finding the country with the max value using Loc
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']


#finding the ratio of gold medal in total
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
# Finding the country with the max value using Loc
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']



# --------------
#Code starts here

data_1 = data[:-1]

data_1['Total_Points'] = 3 * data_1['Gold_Total'] + 2 * data_1['Silver_Total'] + data_1['Bronze_Total']
print(data_1.head())

most_points = max(data_1['Total_Points'])
print(most_points)

best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(best_country)



# --------------
#Code starts here
print(best_country)
print(data.head())

best = data[data['Country_Name'] == best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind='bar',stacked=True,figsize=(10,8))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


