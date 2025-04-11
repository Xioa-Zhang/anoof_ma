maths = int(input("Enter your marks in Mathematics :"))
sci = int(input("Enter you marks in Science :"))
cse = int(input("Enter your marks in Compueter Science and Enginerring :"))
aero = int(input("Enter your marks in Aero_Space :"))
quran = int(input("Enter your marks in Quran :"))
total = maths + sci +cse + aero +quran
average = total/5
if average<35:
    print("Additional Classes were required to Success.")
else:
    print("You were the excellent to go")