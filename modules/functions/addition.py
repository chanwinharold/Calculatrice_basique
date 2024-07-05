def addition():
    a, b, answer = 0, 0, 0  #les variables à utiliser
    print("\nNumber 1 + Number 2 = Answer")
    a = int(input("\nEnter the number 1: "))
    b = int(input("Enter the number 2: "))
    answer = a + b
    return print(f"\n{a} + {b} = {answer}")