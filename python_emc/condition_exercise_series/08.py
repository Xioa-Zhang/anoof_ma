#Task 08
salary = int(input("Enter your Salary amount : "))
age = int(input("Enter your age :"))
if salary>=20000 or age<=25:
    loan_amount = int(input("Enter your loan amount :"))
    if loan_amount>50000:
        print("Maximum Loan Amount is Rs.50 000")
    else:
        print("You are Eligible for this Loan")
else:
    print("You are not Eligible for this Loan")