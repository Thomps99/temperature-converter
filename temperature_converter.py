# temperature_converter.py

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    try:
        value = float(value)
    except ValueError:
        return "Invalid temperature value. Please enter a numerical value."

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'kelvin':
            return celsius_to_kelvin(value)
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'kelvin':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return kelvin_to_celsius(value)
        elif to_unit == 'fahrenheit':
            return kelvin_to_fahrenheit(value)
    else:
        return "Invalid unit. Please enter 'Celsius', 'Fahrenheit', or 'Kelvin'."

def main():
    print("Temperature Converter")
    print("Enter the temperature value, the unit to convert from, and the unit to convert to.")
    value = input("Temperature value: ")
    from_unit = input("Convert from (Celsius, Fahrenheit, Kelvin): ")
    to_unit = input("Convert to (Celsius, Fahrenheit, Kelvin): ")

    result = convert_temperature(value, from_unit, to_unit)
    print(f"Converted temperature: {result}")

if __name__ == "__main__":
    main()
