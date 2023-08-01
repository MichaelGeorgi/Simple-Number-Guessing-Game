"""
--Point Of Game--

--> Generate Random Number
--> Track How Many Trys It Takes For User To Guess Random Number
"""

from GenerateRandomNumber import generate_number

modes = "\nEasy (a), \nMedium (b), \nHard (c)"
print(modes)
num = 0
score = 0
answer = ""
trys = 0

choice = input("Enter Input Here: ").lower()

# Choose Mode
if choice == "a".lower():
    print("\nChoosing Easy Mode...")
    num = 10
elif choice == "b".lower():
    print("\nChoosing Medium Mode...")
    num = 30
elif choice == "c".lower():
    print("\nChoosing Hard Mode")
    num = 50
else:
    print("Unvalid Input")
    
random_number = generate_number(num)

while answer != random_number:
    try:
        answer = int(input("Enter Number: "))
        trys += 1
        if answer != random_number:
            print("Wrong Answer, Try Again.")
    except ValueError:
        print("\nNot A Valid Input")

if answer == random_number:
    print("\nYou Got The Answer In " + str(trys) + " Trys.")