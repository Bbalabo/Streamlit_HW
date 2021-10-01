@st.cache(persist=True)
import pandas as pd
import geopandas as gp
import folium as fo
import streamlit as st
from streamlit_folium import folium_static
import altair as alt
import pydeck as pdk
import numpy as np


## import data
data1 = pd.read_csv('https://raw.github.com/Maplub/odsample/9cfc6ae4dd6a23e874b60b095d9dfcac11cddbed/20190101.csv')
data2 = pd.read_csv('https://raw.github.com/Maplub/odsample/9cfc6ae4dd6a23e874b60b095d9dfcac11cddbed/20190102.csv')
data3 = pd.read_csv('https://raw.github.com/Maplub/odsample/9cfc6ae4dd6a23e874b60b095d9dfcac11cddbed/20190103.csv')
data4 = pd.read_csv('https://raw.github.com/Maplub/odsample/9cfc6ae4dd6a23e874b60b095d9dfcac11cddbed/20190104.csv')
data5 = pd.read_csv('https://raw.github.com/Maplub/odsample/9cfc6ae4dd6a23e874b60b095d9dfcac11cddbed/20190105.csv')

DATE_TIME = "timestart"
data1[DATE_TIME] = pd.to_datetime(data1[DATE_TIME])
data2[DATE_TIME] = pd.to_datetime(data2[DATE_TIME])
data3[DATE_TIME] = pd.to_datetime(data3[DATE_TIME])
data4[DATE_TIME] = pd.to_datetime(data4[DATE_TIME])
data5[DATE_TIME] = pd.to_datetime(data5[DATE_TIME])


data1.drop(['Unnamed: 0','latstop','lonstop','timestop','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11'],axis=1,inplace=True)
data2.drop(['Unnamed: 0','latstop','lonstop','timestop','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13'],axis=1,inplace=True)
data3.drop(['Unnamed: 0','latstop','lonstop','timestop','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11'],axis=1,inplace=True)
data4.drop(['Unnamed: 0','latstop','lonstop','timestop','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11'],axis=1,inplace=True)
data5.drop(['Unnamed: 0','latstop','lonstop','timestop','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11'],axis=1,inplace=True)

# CREATING FUNCTION FOR MAPS

def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lonstartl", "latstartl"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))

# LAYING OUT THE TOP SECTION OF THE APP
row1_1, row1_2 = st.columns((2,3))

with row1_1:
    st.title("BKK Grab Ridesharing Data")
    hour_selected = st.slider("Select hour of pickup", 0, 23)

with row1_2:
    st.write(
    """
    ##
    Examining how Grab pickups vary over time in Bangkok City's.
    By sliding the slider on the left you can view different slices of time and explore different transportation trends.
    """)



# FILTERING DATA BY HOUR SELECTED
data1 = data1[data1[DATE_TIME].dt.hour == hour_selected]
data2 = data2[data2[DATE_TIME].dt.hour == hour_selected]
data3 = data3[data3[DATE_TIME].dt.hour == hour_selected]
data4 = data4[data4[DATE_TIME].dt.hour == hour_selected]
data5 = data5[data5[DATE_TIME].dt.hour == hour_selected]


# SETTING THE ZOOM LOCATIONS 
zoom_level = 12
bkk = [13.7456058, 100.5341187]


st.write('''**All BKK City from %i:00 and %i:00**''' % (hour_selected, (hour_selected + 1) % 24))


#with row3_1:
st.write("** 01 JAN 2019 **" )
map(data1, bkk[0], bkk[1], 11)

#with row4_1:
st.write("** 02 JAN 2019 **" )
map(data2, bkk[0], bkk[1], 11)

#with row5_1:
st.write("** 03 JAN 2019 **" ) 
map(data3, bkk[0], bkk[1], 11)

#with row6_1:
st.write("** 04 JAN 2019 **" )
map(data4, bkk[0], bkk[1], 11)

#with row7_1:
st.write("** 05 JAN 2019 **" )
map(data5, bkk[0], bkk[1], 11)  

st.write('Apisada Taweewong 6130832521')



