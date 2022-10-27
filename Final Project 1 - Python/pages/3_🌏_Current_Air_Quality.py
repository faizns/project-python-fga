import streamlit as st
import requests as r
import pandas as pd
import datetime as dt


# tampilan
st.set_page_config(
    page_title="Current Air Quality",
    page_icon="🌏",
)
st.title("Current Air Quality 🌏")
st.markdown("Want to know what the air quality around the world right now?")

# API request
api_key = 'efa7bcc32b05165f972a5367549d3bd7'
input_location = st.text_input("Enter Location!")

get_location = r.get(f"https://api.openweathermap.org/data/2.5/weather?q={input_location}&appid={api_key}")
data_location = get_location.json()

# SAMPEL >> weather_data
# Enter Location!semarang
# {'coord': {'lon': 110.4203, 'lat': -6.9932}, 'weather': [{'id': 211, 'main': 'Thunderstorm', 'description': 
# 'thunderstorm', 'icon': '11n'}], 'base': 'stations', 'main': {'temp': 302.11, 'feels_like': 305.79, 
# 'temp_min': 302.11, 'temp_max': 302.11, 'pressure': 1008, 'humidity': 70}, 'visibility': 5000, 'wind': 
# {'speed': 1.54, 'deg': 210}, 'clouds': {'all': 40}, 'dt': 1660306462, 'sys': {'type': 1, 'id': 9362, 
# 'country': 'ID', 'sunrise': 1660258058, 'sunset': 1660300764}, 'timezone': 25200, 'id': 1627896, 'name': 
# 'Semarang', 'cod': 200}

# result
if st.button("Search"):
    if data_location['cod'] == '404':
        st.error("City Not Found!")
    else:
        lat = data_location['coord']['lat']
        lon = data_location['coord']['lon']
        
        get_pollution = r.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}")
        data_pollution = get_pollution.json()

        # SAMPEL >> print(data_pollution)
        # {'coord': {'lon': 110.4203, 'lat': -6.9932}, 'list': [{'main': {'aqi': 4}, 'components': {'co': 974.66, 
        # 'no': 0, 'no2': 15.42, 'o3': 56.51, 'so2': 25.75, 'pm2_5': 42.37, 'pm10': 47.76, 'nh3': 6.21}, 'dt': 1660396296}]}

        quality_index = data_pollution['list'][0]['main']['aqi']
        co = data_pollution['list'][0]['components']['co']
        no2 = data_pollution['list'][0]['components']['no2']
        o3 = data_pollution['list'][0]['components']['o3']
        so2 = data_pollution['list'][0]['components']['so2']
        pm25 = data_pollution['list'][0]['components']['pm2_5']
        pm10 = data_pollution['list'][0]['components']['pm10']

        df = pd.DataFrame({
            'Pollutant' : ['NO₂', 'O₃', 'CO', 'SO₂', 'PM₁₀', 'PM₂₅'],
            'Values (μg/m³)' : [no2, o3, co, so2, pm10, pm25],
        })

        def air_index():
            if quality_index == 1:
                st.subheader("Air Quality Index: Good")
                st.markdown("📌 Enjoy activities.")
            elif quality_index == 2:
                st.subheader("Air Quality Index: Fair")
                st.markdown("📌 People unusually sensitive to air pollution: Plan strenuous outdoor activities when air quality is better.")
            elif quality_index == 3:
                st.subheader("Air Quality Index: Moderate")
                st.markdown("📌 Sensitive Groups: Cut back or reschedule strenuous outdoor activities.")
            elif quality_index == 4:
                st.subheader("Air Quality Index: Poor")
                st.markdown("📌 Sensitive groups: Avoid strenuous outdoor activities.")
                st.markdown("📌 Everyone: Cut back or reschedule strenuous outdoor activities.")
            elif quality_index == 5:
                st.subheader("Air Quality Index: Very Poor")
                st.markdown("📌 Sensitive groups: Avoid strenuous outdoor activities.")
                st.markdown("📌 Everyone: Significantly cut back on outdoor physical activities.")
 
        
        now = dt.datetime.now()
        dt_date = (now.strftime("%A, %d %B %Y"))
        dt_time = (now.strftime("Time %H:%M"))


        def result():
            if data_location['cod'] == '404':
                st.error("City Not Found!")
            else:
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("Parameters")
                    st.write(df)
                with col2:
                    st.subheader(dt_date)
                    st.markdown(dt_time)
                    air_index()
                        
        result()