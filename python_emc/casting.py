# Casting ---> Converting one Data_Type to another
n1 = "10"
n2 = "20"
total = n1 + n2
print("Before Casting :",total) # 1020 , because above n1 and n2 arein string dataType

#in casting, we can use string as number also
n1 = int("10")
n2 = int("20")
total = n1 + n2
print("After Casting :",total)

# input() ---> use string as default
n1 = input("Enter the 1st num :")
n2 = input("Enter the 2nd num :")
total = n1 + n2
print(total)

#So, we want to use casting above problem
n1 = int(input("Enter the 1st num :"))
n2= int(input("Enter the 2nd num :"))
total = n1 + n2
print(total)

#Task 01
name = input("Enter your name :")
age = input("Enter your age :")
print("My name is",name)
print("My age is",age )

#Task 02
a = int(input("Enter the value of A :"))
b = int(input("Enter the value of B :"))
c = int(input("Enter the value of C :"))
mul = a*b*c
add = a+b+c
div = mul/add
print(div)

#Task 03
name = input("Enter your name:")
score = int(input("Enter your score :"))
department = input("Enter your Department :")
print("My name is",name)
print("My score is",score/10,"/10")
print("My Department is",department)