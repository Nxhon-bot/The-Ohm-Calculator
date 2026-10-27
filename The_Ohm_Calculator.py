# Welcome to my Ohm Calculator use it when you want. Thanks
# Made by Jhon Bustos JB's


def ask_number(prompt, allow_zero=True):
  # Keep asking until the user enters a valid number
  while True:
    try:
      number = float(input(prompt))
    except ValueError:
      print("Incorrect. Please enter a number.")
      continue

    if not allow_zero and number == 0:
      print("Incorrect. This value can not be 0 (division by zero).")
      continue

    return number


print("Welcome to your favorite calculator: The Ohm Calculator")

while True:
  value = input("Please enter the value you are looking for (R, V, or I):").strip().title()

  # Enter the value of resistance, voltage, or current

  if value == "R":

    x = ask_number("Please enter the voltage (V):")
    y = ask_number("Please enter the current (I):", allow_zero=False)
    z = x / y
    print("The resistance is: ", z, " Ohms")
    break

  elif value == "V":

    x = ask_number("Please enter the resistance (R):")
    y = ask_number("Please enter the current (I):")
    z = x * y
    print("The voltage is: ", z, " Volts")
    break

  elif value == "I":

    x = ask_number("Please enter the voltage (V):")
    y = ask_number("Please enter the resistance (R):", allow_zero=False)
    z = x / y
    print("The current is: ", z, " Amps")
    break

  else:
    print("Incorrect. Input a valid value (R, V, or I).")


print("Thank you for using the Ohm Calculator. Made by JB's")

#Thank for use my program. https://github.com/Nxhon-bot
