import streamlit as st

# tampilan
st.set_page_config(
    page_title= "Temperature Converter",
    page_icon= "🔥",
 )

st.title("Temperature Conversions 🔥")
st.markdown("""
Temperature degrees conversions of Celcius (°C), Reamur (°R), Fahrenheit (°F), and Kelvin (K)
""")

# Konversi Awal CELCIUS
def celcius_to_reamur(input_num):
    return (4 / 5) * input_num

def celcius_to_fahrenheit(input_num):
    return ((9 / 5) * input_num) + 32

def celcius_to_kelvin(input_num):
    return input_num + 273

# Konversi Awal REAMUR
def reamur_to_celcius(input_num): 
    return (5 / 4) * input_num

def reamur_to_fahrenheit(input_num):
    return ((9 / 4) * input_num) + 32

def reamur_to_kelvin(input_num):
    return ((5 / 4) * input_num) + 273

# Konversi Awal FAHRENHEIT
def fahrenheit_to_celcius(input_num):
    return (5 / 9) * (input_num - 32)

def fahrenheit_to_reamur(input_num):
    return (4 / 9) * (input_num - 32)

def fahrenheit_to_kelvin(input_num):
    return ((5 / 9) * (input_num - 32)) + 273

# Konversi Awal Kelvin
def kelvin_to_celcius(input_num):
    return input_num - 273

def kelvin_to_reamur(input_num):
    return (4 / 5) * (input_num - 273)

def kelvin_to_fahrenheit(input_num):
    return ((9 / 5) * (input_num - 273)) + 32

# Membuat box untuk pilihan skala awal
option = st.selectbox(
     'From : ',
     ('Celsius (°C)', 'Reamur (°R)', 'Fahrenheit (°F)', 'Kelvin (K)'))

# Membuat box untuk input nilai
input_num = st.number_input('Value to convert : ')

# Membuat box untuk pilihan skala akhir
convert = st.selectbox(
     'To : ',
     ('Celsius (°C)', 'Reamur (°R)', 'Fahrenheit (°F)', 'Kelvin (K)'))


if st.button('Result'):
    if option == 'Celsius (°C)':
        if convert == 'Celsius (°C)':
            st.success(input_num)
        elif convert == 'Reamur (°R)':
            st.success(celcius_to_reamur(input_num))
        elif convert == 'Fahrenheit (°F)':
            st.success(celcius_to_fahrenheit(input_num))
        elif convert == 'Kelvin (K)':
            st.success(celcius_to_kelvin(input_num))

    elif option == 'Reamur (°R)':
        if convert == 'Celsius (°C)':
            st.success(reamur_to_celcius(input_num))
        elif convert == 'Reamur (°R)':
            st.success(input_num)
        elif convert == 'Fahrenheit (°F)':
            st.success(reamur_to_fahrenheit(input_num))
        elif convert == 'Kelvin (K)':
            st.success(reamur_to_kelvin(input_num))

    elif option == 'Fahrenheit (°F)':
        if convert == 'Celsius (°C)':
            st.success(fahrenheit_to_celcius(input_num))
        elif convert == 'Reamur (°R)':
            st.success(fahrenheit_to_reamur(input_num))
        elif convert == 'Fahrenheit (°F)':
            st.success(input_num)
        elif convert == 'Kelvin (K)':
            st.success(fahrenheit_to_kelvin(input_num))
    
    elif option == 'Kelvin (K)':
        if convert == 'Celsius (°C)':
            st.success(kelvin_to_celcius(input_num))
        elif convert == 'Reamur (°R)':
            st.success(kelvin_to_reamur(input_num))
        elif convert == 'Fahrenheit (°F)':
            st.success(kelvin_to_fahrenheit(input_num))
        elif convert == 'Kelvin (K)':
            st.success(input_num)
