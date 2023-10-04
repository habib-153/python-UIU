choice = int(input("Enter the choice of conversion: "))

if choice == 1:
  # get temperature in Celsius
  celsius = int(input("Enter the temperature in Celsius: "))
  fahrenheit = int(((9*celsius)/5) + 32)
  print(f"The converted temperature is: {fahrenheit} F")

elif choice == 2:
  # get temperature in fahrenheit
  fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
#   formula and calculate
  celsius = int(((fahrenheit-32)*5)/9)
  print(f"The converted temperature is: {celsius} C")

# ------------------------------------------------------------


# if choice == 1:{
#     celsius_temp = float(input("Enter the temperature in Celsius:"))
#     fahrenheit = ((9*celsius_temp)/5)-32
#     print(f"The converted temperature is: {fahrenheit} F")
# }
# 
