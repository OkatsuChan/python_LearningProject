weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? Type (K or L)")
display = f"Your weight is: {round(weight,1)} {unit}"

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight /2.205
    unit = "Kgs."
else:
    display = f"{unit} was not valid"

print(display)
