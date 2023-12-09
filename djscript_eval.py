# Prompt for user input
user_input = input("Enter a number: ")

# Check if the input is a number
try:
   number = float(user_input)
   # Check if the number is positive, negative, or zero
   if number > 0:
       print("You entered a positive number.")
   elif number < 0:
       print("You entered a negative number.")
   else:
       print("You entered zero.")
except:
   print("Invalid input. Please enter a valid number.")