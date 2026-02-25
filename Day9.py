#Lists in python
marks1=94.4
marks2=87.5
marks3=95.6
marks4=66.7
marks=45.8

marks=[94.4,87.5,95.6,66.7,45.8]
print(marks)
print(type(marks))
print(marks[1])
print(marks[0])

student=["vaibhavi",95.4,19,"kumta"]
print(student)
print(type(student))

print(student[0])

#List Slicing
marks=[94.4,87.5,95.6,66.7,45.8]
print(marks[1:4])

marks=[94.4,87.5,95.6,66.7,45.8]
print(marks[1:])

marks=[94.4,87.5,95.6,66.7,45.8]
print(marks[:4])

marks=[94.4,87.5,95.6,66.7,45.8]
print(marks[-3:-1])

marks=[94.4,87.5,95.6,66.7,45.8]
print(marks[-2:-1])

#List Methods
#append
list=[2,1,3]
list.append(4)
print(list)

list=[2,3,4]
list.append(5)
print(list)

#sort
list=[10,9,4]
print(list.sort())
print(list)

list=[30,40,60,70,20]
print(list.sort())
print(list)




