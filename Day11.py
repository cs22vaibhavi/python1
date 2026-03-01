list=[2,1,3,1]
list.remove(1)
print(list)

list=[2,1,9,0]
list.remove(9)
print(list)

#tuples in python
tuple=(2,1,3,1)
print(type(tuple))

tuple=(2,1,3,1)
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple[3])

tup=(1,2,3,4)
print(tup[1:3])

tup=(1,2,3,4)
print(tup[1:2])

#tuple methods
#index
tup=(1,2,3,4)
print(tup.index(2))

tup=(1,2,3,4)
print(tup.index(3))

#count
tup=(1,2,3,4,5,6)
print(tup.count(2))

tup=(1,2,3,4,5,6)
print(tup.count(3))

#practise question
#to print 3 movies store them in a list
m1=str(input("enter movie1 name:"))
m2=str(input("enter movie2 name:"))
m3=str(input("enter movie3 name:"))
print([m1],[m2],[m3]) 

#palindrome programme
list1=[1,2,1]

print(list1.copy())
print(list1.reverse())

if(list1==list1):
    print("palindrome")
else:
    print("Not palindrome")

