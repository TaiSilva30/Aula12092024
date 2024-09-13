def celsius_fahrenheit(temp_celsius):
    return (temp_celsius * 1.8) + 32 
def fahrenheit_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) / 1.8

temp_celsius = float(input("informe a temperatura em graus celsius: "))
print(f"a temperatura é {celsius_fahrenheit(temp_celsius)} em fahrenheit")

temp_fahrenheit = float(input("informe a temperatura em graus fahrenheit: "))
print(f"a temperatura é {fahrenheit_celsius(temp_fahrenheit)} em celsius")