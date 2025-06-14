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

def convert_temperature():
    print("Temperature Converter")
    print("Enter the temperature value followed by its unit (C, F, or K):")
    
    try:
        temp_input = input("Example: 25 C, 77 F, or 300 K: ").strip().split()
        temp_value = float(temp_input[0])
        temp_unit = temp_input[1].upper()
        
        if temp_unit == "C":
            print(f"{temp_value}°C is equivalent to:")
            print(f"{celsius_to_fahrenheit(temp_value):.2f}°F")
            print(f"{celsius_to_kelvin(temp_value):.2f} K")
        elif temp_unit == "F":
            print(f"{temp_value}°F is equivalent to:")
            print(f"{fahrenheit_to_celsius(temp_value):.2f}°C")
            print(f"{fahrenheit_to_kelvin(temp_value):.2f} K")
        elif temp_unit == "K":
            print(f"{temp_value} K is equivalent to:")
            print(f"{kelvin_to_celsius(temp_value):.2f}°C")
            print(f"{kelvin_to_fahrenheit(temp_value):.2f}°F")
        else:
            print("Invalid unit! Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
    except (ValueError, IndexError):
        print("Invalid input! Please enter a valid temperature and unit.")

# Run the program
convert_temperature()
