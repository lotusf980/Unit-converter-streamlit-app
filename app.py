import streamlit as st

# Conversion data
unit_categories = {
    "Length": {
        "Meter": 1.0, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1.0, "Gram": 1000, "Milligram": 1000000, "Pound": 2.20462, "Ounce": 35.274
    },
    "Area": {
        "Square Meter": 1.0, "Square Kilometer": 0.000001, "Square Mile": 3.861e-7,
        "Square Yard": 1.19599, "Square Foot": 10.7639, "Square Inch": 1550.0, 
        "Hectare": 0.0001, "Acre": 0.000247105
    },
    "Volume": {
        "Liter": 1.0, "Milliliter": 1000, "Cubic Meter": 0.001, "Gallon (US)": 0.264172, "Pint": 2.11338
    },
    "Temperature": {
        "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"
    },
    "Speed": {
        "Meter per second": 1.0, "Kilometer per hour": 3.6, "Mile per hour": 2.23694, "Knot": 1.94384
    },
    "Time": {
        "Second": 1.0, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400
    },
    "Pressure": {
        "Pascal": 1.0, "Bar": 1e-5, "Atmosphere": 9.8692e-6, "PSI": 0.000145038
    },
    "Energy": {
        "Joule": 1.0, "Kilojoule": 0.001, "Calorie": 0.239006, "Kilowatt-hour": 2.7778e-7
    },
    "Frequency": {
        "Hertz": 1.0, "Kilohertz": 0.001, "Megahertz": 1e-6, "Gigahertz": 1e-9
    },
    "Fuel Economy": {
        "Kilometers per liter": 1.0, "Miles per gallon (US)": 2.35215, "Miles per gallon (UK)": 2.82481
    },
    "Mass": {
        "Kilogram": 1.0, "Gram": 1000, "Milligram": 1e6, "Metric ton": 0.001, "Pound": 2.20462, "Ounce": 35.274
    },
    "Plane Angle": {
        "Degree": 1.0, "Radian": 0.0174533, "Gradian": 1.11111
    },
    "Digital Storage": {
        "Bit": 1.0, "Byte": 0.125, "Kilobyte": 0.000125, "Megabyte": 1.25e-7, "Gigabyte": 1.25e-10,
        "Terabyte": 1.25e-13
    },
    "Data Transfer Rate": {
        "Bit per second": 1.0, "Kilobit per second": 0.001, "Megabit per second": 1e-6,
        "Gigabit per second": 1e-9, "Terabit per second": 1e-12
    }
}

# Temperature conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value  # Same unit conversion

# General unit conversion function
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    else:
        return value * (unit_categories[category][to_unit] / unit_categories[category][from_unit])

# Streamlit UI
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🔄 Google-Style Unit Converter")

# Select category
category = st.selectbox("Choose a category:", list(unit_categories.keys()))

# Select units
from_unit = st.selectbox("From:", list(unit_categories[category].keys()))
to_unit = st.selectbox("To:", list(unit_categories[category].keys()))

# Input value
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Convert button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")