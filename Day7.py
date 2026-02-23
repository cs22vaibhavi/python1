#Conditional statement
#if
age=21

if(True):
    print("can vote and apply for license")
    print("can drive")

#elif
light="green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light=="yellow"):
    print("look")

print("end of code")

#else
num=5

if(num>10):
    print("greater than 2")
elif(num>20):
    print("greater than 3")
else:
    print("Not greater than 2")

#example 1
light="green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")


#example2
age=24

if(age>18):
    print("can vote") #indentation
else:
    print("cannot vote")


#practise work
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

#or
marks=int(input("enter your marks:"))
marks=80
if(marks>90):
    grade="A"
elif(marks>80 and marks<90):
    grade="B"
elif(marks>70 and marks<80):
    grade="c"
else:
    grade="D"

print("grade of the student",grade)

#nesting

age=34

if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

