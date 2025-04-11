#Task 06 ---. mini_calculator
n1 = int(input("Enter your 1st num :"))
n2 = int(input("Enter your 2nd num :"))
print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")
choice = int(input("Enter your Choice :"))
if choice == 1:
    print(n1+n2)
elif choice == 2:
    print(n1 - n2)
elif choice == 3:
    print(n1*n2)
else:
    print(n1/n2)
