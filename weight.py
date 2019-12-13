weight = int(input('Weight: '))
unit = input('Lbs or Kg: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == "K":
    converted = weight/0.45
    print(f"You are {converted} pounds")
else:
    print("provide valid choice")

