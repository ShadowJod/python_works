# this is all about string and string function

str= "my name is nikhil"
print(str)
print(str.endswith("l"))
print(str.capitalize())
print(str.replace("n","g"))
print(str.find("nikhil"))
print(str.count("n"))


no = input("enter your name  ")
print("length of your name: " ,len(no))


int = int(input("enter your number  "))
rem = int % 2

if(rem == 0):
    print("this is even number")

else:
    print("this is odd number")

a = int(input("enter first number "))
b = int(input("enter second number "))
c = int (input("enter the third number "))

if(a>=b and a>=c):
    print(" a is the greatest")

elif(b>=a and b>=c):
    print("b is the grestest")

else:
    print("c is the greatest")


int = int(input("enter your number"))
if(int % 7 == 0):
    print("this number is divisible by 7")

else:
    print("this number is not divisible by 7")