# Import our math module
import MathModule


print("Hello! Welcome to Star Calculator. Please say 2 numbers for calculation.")

# Input a number for calculate
firstNumber = input("Please say first number   ")
secondNumber = input("Please say second number   ")

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

# Input a action for calculate
action = input("Please specify what action you want to take \n Say A for add \n Say S for subtract \n Say D for divide \n Say M for multiply \n Say E for exponentiation \n")

# I'm making all the letters small because I don't want any mistakes
action = str(action)
action = action.lower()

# We call our module according to the selected process
if action == "a" :
    MathModule.add(firstNumber,secondNumber)
elif action == "s" :
    MathModule.subtract(firstNumber,secondNumber)
elif action == "d" : 
    MathModule.divide(firstNumber,secondNumber)
elif action == "m" :
    MathModule.multiply(firstNumber,secondNumber)
elif action == "e" :
    MathModule.exponentiation(firstNumber,secondNumber)
else :
    print("Please select a valid option")


# We question its accuracy
truth = input("Is the result of the operation correct? \n(T/F)")
truth = truth.lower()

if truth == "t" :
    print("Thanks for choosing me")
elif truth == "f" :
    print("Oww i'm sorry for wrong result. Please contact my developer \nMail : guneslikoray@gmail.com")
else:
    print("Please select a valid option")
