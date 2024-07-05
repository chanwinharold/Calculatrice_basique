from modules.functions.addition import addition
from modules.functions.soustraction import subtract
from modules.functions.multiplication import multiply
from modules.functions.division import divide
def main():

    print("***Calculator ©2024***\nChoose a function:")
    choice = input("1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n Give your answer with a number: ")
    while (choice not in ('1', '2', '3', '4')):
        print("\nPlease enter a number between 1 and 4")
        choice = input("1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n Give your answer with a number: ")
    if(choice == '1'):
        addition()
    elif(choice == '2'):
        subtract()
    elif(choice == '3'):
        multiply()
    elif(choice == '4'):
        divide()

main()

while(True):
    print("\nDo you want to restart the program? (y/n)")
    choice = input()

    while(choice not in ['y', 'n']):
        print("\nPlease enter y or n")
    if(choice == "y"):
        main()
    elif(choice == "n"):
        print("Thank you for using this program\n")
        exit()

