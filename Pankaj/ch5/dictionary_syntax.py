myDict ={
    "Fast" :"in a quick manner",
    "pankaj":"a coder",
    "deepak":{"teacher":"english"}
}

print (myDict['Fast'])
print (myDict['pankaj'])
print (myDict['deepak'])
print (myDict['deepak']['teacher'])
myDict['deepak']['teacher']="physics" #to change the value in key
print (myDict['deepak']['teacher'])

