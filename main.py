
import streamlit as st

conversions = {
    "Length": {
        "meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084, "inches": 39.37007874, "centimeters": 100, "millimeters": 1000, "yards": 1.0936133, "micrometers": 1_000_000,  # Added (1 meter = 1,000,000 micrometers)
    "nanometers": 1_000_000_000,  # Added (1 meter = 1,000,000,000 nanometers)
    },
    "Weight": {
        "grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274, "milligrams": 1000, "stones": 0.000157473, "tons": 0.000001
    },
    "Temperature": {
    # Celsius (Base Unit)
    "Celsius": lambda x: x,

    # Fahrenheit
    "Fahrenheit": lambda x: (x * 9/5) + 32,  # °C to °F

    # Kelvin
    "Kelvin": lambda x: x + 273.15,  # °C to K

    # Rankine
    "Rankine": lambda x: (x + 273.15) * 9/5,  # °C to °R

    # Delisle
    "Delisle": lambda x: (100 - x) * 3/2,  # °C to °De

    # Newton
    "Newton": lambda x: x * 33/100,  # °C to °N
},

    "Volume": {
        # Metric Units
    "cubic_meters": 1,  # Base unit
    "liters": 1000,  # 1 cubic meter = 1000 liters
    "milliliters": 1_000_000,  # 1 cubic meter = 1,000,000 milliliters

    # US Customary Units
    "us_gallons": 264.172052,  # 1 cubic meter = 264.172052 US gallons
    "us_quarts": 1056.6882094326,  # 1 cubic meter = 1056.688209 US quarts
    "us_pints": 2113.3764188652,  # 1 cubic meter = 2113.376418 US pints
    "us_legal_cups": 4166.6666666667,  # 1 cubic meter = 4166.67 US legal cups
    "us_fluid_ounces": 33814.022701843,  # 1 cubic meter = 33,814.0227 US fluid ounces
    "us_tablespoons": 67628.045403686,  # 1 cubic meter = 67,628.0454 US tablespoons
    "us_teaspoons": 202884.136211058,  # 1 cubic meter = 202,884.1362 US teaspoons

    # Imperial (UK) Units
    "imperial_gallons": 219.96924829909,  # 1 cubic meter = 219.969248 Imperial gallons
    "imperial_quarts": 879.87699319636,  # 1 cubic meter = 879.876993 Imperial quarts
    "imperial_pints": 1759.75398639272,  # 1 cubic meter = 1759.753986 Imperial pints
    "imperial_cups": 3519.50797,  # 1 cubic meter = 3519.507973 Imperial cups
    "imperial_fluid_ounces": 35195.0797278544,  # 1 cubic meter = 35,195.0797 Imperial fluid ounces
    "imperial_tablespoons": 56312.1275645671,  # 1 cubic meter = 56,312.1276 Imperial tablespoons
    "imperial_teaspoons": 168936.383,  # 1 cubic meter = 168,936.383 Imperial teaspoons

    # Cubic Measurements
    "cubic_inches": 61023.7440947323,  # 1 cubic meter = 61,023.7441 cubic inches
    "cubic_feet": 35.314666721489,  # 1 cubic meter = 35.3146667 cubic feet
    "cubic_yards": 1.3079506193144  # 1 cubic meter = 1.30795062 cubic yards
    },
    "Area": {
        "square meters": 1, "square kilometers": 0.000001, "square miles": 3.861e-7, "square feet": 10.7639, "square inches": 1550, "hectares": 0.0001, "acres": 0.000247105, "square yards": 1.19599
    },
    "Data Transfer Rate": {
        "bps": 1, "Bps": 0.125, "Kbps": 0.001, "Kibps": 0.000976563, "Mbps": 0.000001, "Mibps": 9.5367e-7, "Gbps": 0.000000001, "Gibps": 9.3132e-10, "Tbps": 0.000000000001, "Tibps": 9.0949e-13, "Pbps": 0.000000000000001, "Pibps": 8.8818e-16, "KBps": 0.000125, "KiBps": 0.00012207, "MBps": 1.25e-7, "MiBps": 1.1921e-7, "GBps": 1.25e-10, "GiBps": 1.1642e-10, "TBps": 1.25e-13, "TiBps": 1.1369e-13, "PBps": 1.25e-16, "PiBps": 1.1259e-16
    },
    "Digital Storage": {
        "bits": 1, "bytes": 0.125, "kilobytes": 0.000125, "megabytes": 1.25e-7, "gigabytes": 1.25e-10, "terabytes": 1.25e-13
    },
    "Energy": {
        "joules": 1, "kilojoules": 0.001, "calories": 0.239006, "kilocalories": 0.000239006, "watt-hours": 0.000277778, "kilowatt-hours": 2.7778e-7
    },
    "Frequency": {
        "hertz": 1, "kilohertz": 0.001, "megahertz": 0.000001, "gigahertz": 0.000000001
    },
    "Fuel Economy": {
        "mpg": 1, "kmpl": 0.425144, "l/100km": 235.215
    },
    "Plane Angle": {
        "degrees": 1, "radians": 0.0174533, "gradians": 1.11111
    },
    "Pressure": {
        "pascals": 1, "kilopascals": 0.001, "bars": 0.00001, "psi": 0.000145038
    },
    "Speed": {
        "meter_per_second": 1,  # Base unit (m/s)
        "kilometer_per_hour": 3.6,  # 1 m/s = 3.6 km/h (exact)
        "mile_per_hour": 2.23694,  # 1 m/s ≈ 2.23694 mph (rounded to 5 decimal places)
        "knot": 0.514444,  # 1 m/s ≈ 1.94384 knots (rounded to 5 decimal places)
        "foot_per_second": 3.28084,  # 1 m/s ≈ 3.28084 ft/s (rounded to 5 decimal places)
        "kilometer_per_second": 0.001,  # 1 m/s = 0.001 km/s (exact)
        "centimeter_per_second": 100,  # 1 m/s = 100 cm/s (exact)
        "speed_of_sound": 0.00291545,  # 1 m/s ≈ 0.00291545 Mach (at 20°C in dry air, 343 m/s = Mach 1)
        "speed_of_light": 3.33564e-9,  # 1 m/s ≈ 3.33564 × 10⁻⁹ c (c = 299,792,458 m/s, exact)
    },
    "Time": {
        "seconds": 1,
        "milliseconds": 1000,
        "microseconds": 1000000,
        "nanoseconds": 1000000000,
        "minutes": 1/60,  # More precise
        "hours": 1/3600,  # 1/3600 instead of 0.000277778
        "days": 1/86400,  # 1/86400 instead of 0.0000115741
        "weeks": 1/604800,  # 1/604800 instead of 0.0000016534
        "months": 1/2629800,  # Approximate (30.44 days per month)
        "years": 1/31557600,  # 365.25 days per year
        "decades": 1/315576000,  # 10 years
        "centuries": 1/3155760000  # 100 years
    }
}


def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius":
            result = conversions[category][to_unit](value)
        elif from_unit == "Fahrenheit":
            result = (
                (value - 32) * 5/9 if to_unit == "Celsius" else
                ((value - 32) * 5/9) + 273.15 if to_unit == "Kelvin" else
                (value + 459.67) * 5/9 if to_unit == "Rankine" else
                (100 - ((value - 32) * 5/9)) * 3/2 if to_unit == "Delisle" else
                ((value - 32) * 5/9) * 33/100 if to_unit == "Newton" else
                value
            )
        elif from_unit == "Kelvin":
            result = (
                value - 273.15 if to_unit == "Celsius" else
                ((value - 273.15) * 9/5) + 32 if to_unit == "Fahrenheit" else
                value * 9/5 if to_unit == "Rankine" else
                (100 - (value - 273.15)) * 3/2 if to_unit == "Delisle" else
                (value - 273.15) * 33/100 if to_unit == "Newton" else
                value
            )
        elif from_unit == "Rankine":
            result = (
                (value - 491.67) * 5/9 if to_unit == "Celsius" else
                value * 5/9 if to_unit == "Kelvin" else
                (value - 459.67) if to_unit == "Fahrenheit" else
                (100 - ((value - 491.67) * 5/9)) * 3/2 if to_unit == "Delisle" else
                ((value - 491.67) * 5/9) * 33/100 if to_unit == "Newton" else
                value
            )
        elif from_unit == "Delisle":
            result = (
                100 - (value * 2/3) if to_unit == "Celsius" else
                ((100 - (value * 2/3)) * 9/5) + 32 if to_unit == "Fahrenheit" else
                (100 - (value * 2/3)) + 273.15 if to_unit == "Kelvin" else
                ((100 - (value * 2/3)) + 273.15) * 9/5 if to_unit == "Rankine" else
                (100 - (value * 2/3)) * 33/100 if to_unit == "Newton" else
                value
            )
        else:
            result = value  # If no valid conversion is found, return the input value

        # Format result to remove unnecessary decimal places
        return round(result, 2) if isinstance(result, float) else result

    else:
        # Handle speed_of_light separately
        if category == "Speed" and to_unit == "speed_of_light":
            # Convert from_unit to m/s first
            value_in_mps = value * conversions[category][from_unit]
            # Convert m/s to speed_of_light
            result = value_in_mps * conversions[category][to_unit]
        else:
            result = value * conversions[category][to_unit] / conversions[category][from_unit]

        # Return result with appropriate precision
        if abs(result) < 1e-6:  # For very small numbers, use scientific notation
            return f"{result:.6e}"
        else:
            return round(result, 6)


st.title("Unit Converter")

category = st.selectbox("Select Category", list(conversions.keys()))

units = {category: list(conversions[category].keys()) for category in conversions}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter Value", value=1, step=1)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} is equal to {result} {to_unit}")
