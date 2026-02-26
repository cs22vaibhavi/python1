#revision
print("hello world");

a=10
b=50
sum=a+b
dif=a-b
mul=a*b
div=a/b
print(sum)
print(dif)
print(mul)
print(div)

name=input("enter name:")
age=int(input("enter age:"))
marks=float(input("enter marks:"))
print("welcome",name)
print("age=",age)
print("marks=",marks)

str1="vaibhavi"
str2="Radhakrishna"
str3="shanbhag"
ch1=str1[3]
ch2=str2[4]
ch3=str3[2]
print(ch1)
print(ch2)
print(ch3)
print(len(str1))
print(len(str2))
print(len(str3))

name=str(input("enter fisrst name:"))
print(len(name))

marks=50

if(marks>90):
    print("Grade A")
elif(marks>80):
    print("Grade B")
elif(marks>70):
    print("Grade c")
elif(marks>60):
    print("grade d")
else:
    print("Fail") 

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


#List Slicing
marks=[94.4,87.5,95.6,66.7,45.8]
print(marks[1:4])

#List Methods
#append
list=[2,1,3]
list.append(4)
print(list)

list=[10,9,4]
print(list.sort())
print(list)

