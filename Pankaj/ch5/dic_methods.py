myDict ={
    "Fast" :"in a quick manner",
    "pankaj":"a coder",
    "deepak":{"teacher":"english"}, 
    "marks":[21,23,43,44,54],
    1:2
}
print(myDict.keys())  # to print all keys 
print(myDict.values())# to print values of keys
print(myDict.items()) # to print (key,values) of all contents of dictionary
print(myDict)
newDict= {
    "ajay" : "doctor"
}
myDict.update(newDict) #to update new dictionary into old dictionary
print(myDict)
# the difference between .get function and [] to acces values
print(myDict.get("harry")) #return none if value not present
print(myDict["harry2"])#through an error 
#for more methods search dictionary methods on python.com-> doc

