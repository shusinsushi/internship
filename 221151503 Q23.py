def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit.upper() == 'C':
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F.")
elif unit.upper() == 'F':
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C.")
else:
    print("Please enter a valid temperature unit (C or F).")
