def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# Test
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(fahrenheit_to_celsius(32))