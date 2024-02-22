# Defining a function to perform the calculation based on the operation choice
def calculate(num1, num2, choice):
  if choice == "+":
    return num1 + num2
  elif choice == "-":
    return num1 - num2
  elif choice == "*":
    return num1 * num2
  elif choice == "/":
    return num1 / num2
  elif choice == "%":
    return num1 % num2
  elif choice == "**":
    return num1 ** num2
  else:
    return "Wrong Move, Soldier!"

# Initializing a variable to store the user's choice to continue or exit
continue_calculation = "y"

# Using a while loop to repeat the calculation until the user chooses to exit
while continue_calculation == "y":
  # Prompting the user to input two numbers and an operation choice
  num1 = float(input("Enter Your First Choice: "))
  num2 = float(input("Enter Your Second Choice: "))
  choice = input("Enter Your Favourite Operation (+, -, *, /, %, **): ")

  # Calling the calculate function and display the result
  result = calculate(num1, num2, choice)
  print(f"Hurrah! The result of {num1} {choice} {num2} is {result}")

  # Asking the user if they want to continue or exit
  continue_calculation = input("Soldier! Do you want to continue the calculation? (y/n): ")

  # Validating the user's input
  while continue_calculation not in ["y", "n"]:
    print("Wrong Move, Soldier! Please enter y or n to continue your calculation.")
    continue_calculation = input("Soldier! Do you want to continue the calculation? (y/n): ")

# Printing a farewell message when the user exits the program
print("Thank you for using the calculator. Have a nice day, Soldier!")
