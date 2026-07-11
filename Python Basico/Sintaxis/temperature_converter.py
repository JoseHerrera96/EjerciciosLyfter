# Input: temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Conversions
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Output: show three values
print("\nResults:")
print(f"Celsius:    {celsius:.2f} °C")
print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Kelvin:     {kelvin:.2f} K")