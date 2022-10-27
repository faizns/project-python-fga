import streamlit as st
import requests as r
import datetime as dt

# tampilan
st.set_page_config(
    page_title="Current Weather",
    page_icon="⛅",
)
st.title("Current Weather ⛅")
st.markdown("Want to know what the weather around the world right now?")


#  API request
api_key = 'efa7bcc32b05165f972a5367549d3bd7'

input_location = st.text_input("Enter Location!")

get_data = r.get(f"https://api.openweathermap.org/data/2.5/weather?q={input_location}&appid={api_key}")
data = get_data.json()

# SAMPEL >> weather_data
# Enter Location!semarang
# {'coord': {'lon': 110.4203, 'lat': -6.9932}, 'weather': [{'id': 211, 'main': 'Thunderstorm', 'description': 
# 'thunderstorm', 'icon': '11n'}], 'base': 'stations', 'main': {'temp': 302.11, 'feels_like': 305.79, 
# 'temp_min': 302.11, 'temp_max': 302.11, 'pressure': 1008, 'humidity': 70}, 'visibility': 5000, 'wind': 
# {'speed': 1.54, 'deg': 210}, 'clouds': {'all': 40}, 'dt': 1660306462, 'sys': {'type': 1, 'id': 9362, 
# 'country': 'ID', 'sunrise': 1660258058, 'sunset': 1660300764}, 'timezone': 25200, 'id': 1627896, 'name': 
# 'Semarang', 'cod': 200}

# Enter Location!ssmarga ------- typo/invalid location
# {'cod': '404', 'message': 'city not found'}

# result
if st.button("Search"):
    if data['cod'] == '404':
        st.error("City Not Found!")
    else:
        # description
        weather = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        image = "![Alt Text]"+"(http://openweathermap.org/img/wn/"+ icon +"@2x.png)"
        
        # parameters
        temp = round((data['main']['temp'])-273)
        humi = data['main']['humidity']
        wind = data['wind']['speed']
       
        # date/time
        now = dt.datetime.now()
        dt_date = (now.strftime("%A, %d %B %Y  |  Time %H:%M"))
       

        # layout 
        col_a, col_b = st.columns(2)
        with col_a :
            st.subheader(weather)
            st.caption(dt_date)
        with col_b :
            st.markdown(image, unsafe_allow_html=False)

        col_1, col_2, col_3 = st.columns(3)
        col_1.metric("Temperature", f"{temp}°C")
        col_2.metric("Wind", f"{wind}mph")
        col_3.metric("Humidity", f"{humi}%")
