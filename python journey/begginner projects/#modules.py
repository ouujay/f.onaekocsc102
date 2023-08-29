'''mylist = ["bannana", "cherry", "apple"]
b = input("wha are you looking for: ")
mylist.append(b)
if b in mylist:
    print(f"yes {b} is there")
else:
    print("its not available at the moment")

print(mylist)'''
#list ordered mutable allows dubliate element
'''mylist =[1,2,3,4,5,6,7,8,9]

a = mylist[1:5]
print(a)'''
# this is finding the square of a list
''''mylist =[1,2,3,4,5,6]
b = [i*i for i in mylist]

print(mylist)
print(b)'''

"""mytuple = ('max' , 28 , 'boston') 
print()"""

my_tuple = (0, 1, 2, 5, 3, 4)


i1, *i2, i4, i3 = my_tuple

print(i2)

