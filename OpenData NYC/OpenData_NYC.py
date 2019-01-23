import folium as fd
import pandas as pd
import matplotlib as mat
import geocoder as geo

#index for dataset format

df = pd.read_csv('Value_of_Energy_Cost_Savings_Program_Savings_for_Businesses.csv')
df = df[['Latitude','Longitude']]

cd = pd.read_csv('Value_of_Energy_Cost_Savings_Program_Savings_for_Businesses.csv')
cd = cd[['Company Name','Industry','Latitude','Longitude']]

#List All Lat & Long Values for df
df = df[df['Latitude'].notnull() & df['Longitude'].notnull()]
list_of_coordinates = df.values.tolist()
print(list_of_coordinates)
print(cd)


#Create Map Object
m = fd.Map(location=[40.745706, -73.929565], zoom_start=10)

m.save('OpenData.html')

#Global Tooltip
tooltip = 'Click or Tap for more information'

#Manufacturing = Red
#Wholesale= Blue
#Commercial= Green
#Create Markers
fd.Marker([40.717634, -74.002233],
              popup='<strong> GENERAL HARDWARE MANUFACTURING </strong>', #Html Paragraph Statement
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.665231, -73.998209],
              popup='<strong>  FEDERAL EXPRESS </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='blue')).add_to(m),
fd.Marker([40.722201, -74.008204],
              popup='<strong> PRINT 2 PRINT LLC </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.752098, -74.002999],
              popup='<strong>  GOTHAM SEAFOOD CORP.  </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.735203, -73.987898],
              popup='<strong>  ELENI''S NYC, INC </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.760184, -73.975548],
              popup='<strong>  Rolex Watch USA, Inc. </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='green')).add_to(m),
fd.Marker([40.660096, -73.997405],
              popup='<strong>  ALADDIN BAKERS, INC/Bread Head, LLC. </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.754384, -73.992742],
              popup='<strong>  New Concepts of NY LLC 	  </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.812964, -73.953759],
              popup='<strong> Aids Vaccine Advocacy Coalition </strong>', #Html Paragraph Statement
              tooltip=tooltip,
              icon=fd.Icon(color='green')).add_to(m),
fd.Marker([40.812964, -73.953759],
              popup='<strong>  Neighborhood Eigth Avenue LLC </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='green')).add_to(m),
fd.Marker([40.802355, -73.940987],
              popup='<strong> G & J WHOLESALE ASSOCIATES, LLC </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='blue')).add_to(m),
fd.Marker([40.802879, -73.940604],
              popup='<strong>  Red Rabbit LLC 	 </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.812964, -73.953759],
              popup='<strong>  Graham Windham Organization </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='blue')).add_to(m),
fd.Marker([40.725775, -73.989718],
              popup='<strong>  REGAL HOME COLLECTIONS. </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.814216, -73.95564],
              popup='<strong>  B.E.L.L. Foundation  </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='purple')).add_to(m),
fd.Marker([40.812648, -73.954391],
              popup='<strong> HOME ENTERTAINMENT DESIGN, INC. </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.812964, -73.953759],
              popup='<strong> Urban Electric Power, LLC  </strong>', #Html Paragraph Statement
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.75886, -73.984843],
              popup='<strong>  RWS & Associates Entertainment 	</strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='blue')).add_to(m),
fd.Marker([40.836017, -73.947563],
              popup='<strong> Hudson Moving & Storage Co., Inc </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.80599, -73.955068],
              popup='<strong>  Office 118 Equities LLC 	  </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='purple')).add_to(m),
fd.Marker([40.746364, -73.995088],
              popup='<strong>  221 WEST 26TH STREET CORP. </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.814216, -73.95564],
              popup='<strong>  Chromation, Inc. </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='green')).add_to(m),
fd.Marker([40.812964, -73.953759],
              popup='<strong>  WHBI LLC  </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='green')).add_to(m),
fd.Marker([40.812964,-73.953759],
              popup='<strong>  The Gluck Architectural Collaborative, P.C.   </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='green')).add_to(m),
fd.Marker([40.867709, -73.929902],
              popup='<strong>  MAGIC NOVELTY CO., INC.	</strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.802929, -73.940568],
              popup='<strong> FAT WITCH BAKERY, INC.  </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.665231, -73.99820],
              popup='<strong>  FEDERAL EXPRESS   </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='green')).add_to(m),
fd.Marker([40.741876, -74.004713],
              popup='<strong>  HALE & HEARTY SOUPS, LLC  </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),
fd.Marker([40.814216, -73.95564],
              popup='<strong>  JANUS MANAGEMENT, INC. 	 </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='purple')).add_to(m),
fd.Marker([40.812887, -73.953622],
              popup='<strong>  Duce Construction Corp. </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='green')).add_to(m),
fd.Marker([40.742976, -73.988539],
              popup='<strong>  PENTAGRAM DESIGN, INC  </strong>',
              tooltip=tooltip,
              icon=fd.Icon(color='red')).add_to(m),

m.save('OpenData.html')


#Industries
#1. Commercial -
#2. LandLord -
#3. Manufacturing -
#4. Other -
#5. Public Benefits -
#6. WholeSale/Warehouses/Distribution -






#Generate the map

