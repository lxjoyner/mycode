#! /usr/bin/env python3
# A program that prompts a user for two operators and operations (plus or minus)
# the projram then shows the result.
# The user may enter q to exit the program.

calc1 = 0.0
calc2 = 0.0
operation = ""

while (calc1 != "q"):
   print("What is the first operator? or, enter q to quit: ")
   calc1 = raw_input()
   if calc1 == "Q":
       break
   calc1 = float(calc1)
   print("What is the second operator? Or, enter q to quit: ")
   calc2 = raw_input()
   if calc2 == "q":
       break
   calc2 = float(calc2)
   print("Enter an operation to perform on the two operators (+ or -): ")
   operation = raw_input()
   if operation == "+":
       print("" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2)

   elif operation == '-':
       print("" + str(calc1) + "-" + str(calc2) + " = " + str(calc1 - calc2))
   else:
       print(" Not a valid entry. Restarting...")

