
# creating an empty set
b=set()
print(type(b))

# adding values in a set
b.add(1)
b.add(2)
b.add(3)
b.add(5)
b.add(5)
b.add({2:5}) # cannot add list and dictionary in sets
print(b)
print(len(b))# print the length og set
b.remove(5)# to remove item from sets
print(b) 
print(b.pop())#to pick a random number
print(b)
b.clear()#empty b 
print(b.intersection({2,6}))
