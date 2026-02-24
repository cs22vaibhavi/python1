#WAP to print given number is odd or even
num=32

rem=num%2

if(rem==0):
    print("even")
else:
    print("odd")


#another method
num=23

if(num % 2== 0):
    print("EVEN")
else:
    print("ODD")


#WAP to find the greatest of 3 numbers entered by the user

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if(a>=b and a>=c):
    print("first number is greatest",a)
elif(b>=c and b>a):
    print("second number is greatest",b)
else:
    print("third is largest",c) 


#WAP TO FIND THE GREATEST OF 4 NUMBERS

a=int(input("enter first number:"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))

if(a>b and a>c and a>d):
    print("first number is greatest",a)
elif(b>c and b>d and b>a):
    print("second number is greatest",b)
elif(c>d and c>a and c>b):
    print("third number is greatest",c)
else:
    print("fourth number is greatest",d) 

#WAP TO FIND THE GREATEST OF 4 NUMBERS
a=int(input("enter first number:"))
b=int(input("enter second number:"))

if(a>b):
    print("first number is greatest",a)
else:
    print("second number is greatest",b) 

#WAP TO FIND THE Smallest OF 4 NUMBERS

a=int(input("enter first number:"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))

if(a<b and a<c and a<d):
    print("first number is smallest",a)
elif(b<c and b<d and b<a):
    print("second number is smallest",b)
elif(c<d and c<a and c<b):
    print("third number is smallest",c)
else:
    print("fourth number is smallest",d)

#WAP TO check if a number is multiple of 7 or not
x=int(input("enter a number:"))

if(x%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")

#WAP TO check if a number is multiple of 6 or not
num=int(input("enter a number:"))

if(num%6==0):
    print("multiple of 6")
else:
    print("not a multiple of 6")
