def divide():
    a, b, answer = 1, 1, 1 #les variables à utiliser
    print("\nNumber 1 ÷ Number 2 = Answer")
    a = int(input("\nEnter the number 1: "))
    b = int(input("Enter the number 2: "))
    if (b == 0 ):
        print("\nUnable to divide, cause the divisor cannot be null, Please enter a number not null")
        divide()
    answer = a / b
    return print(f"\n{a} ÷ {b} = {answer}")