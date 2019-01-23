import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Value_of_Energy_Cost_Savings_Program_Savings_for_Businesses.csv')
df = df[['Company Name','Industry','Latitude','Longitude']]

print(df)

#Create Map Object
m = folium.Map(location=[40.745706, -73.929565], zoom_start=10)

for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']],
                  popup=row['Latitude'],
                  icon=folium.Icon(color='red')
                  ).add_to(m)

m.save('OpenDataMap.html')
