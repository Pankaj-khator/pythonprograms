myDict={}
a=input("FIRST FRIEND ENTER YOUR NAME PLEASE   ")
b=input("FIRST FRIEND ENTER YOU FAV LANGUAGE   ")

c=input("SECOND FRIEND ENTER YOUR NAME PLEASE   ")
d=input("SECOND FRIEND ENTER YOU FAV LANGUAGE   ")

e=input("THIRD FRIEND ENTER YOUR NAME PLEASE   ")
f=input("THIRD FRIEND ENTER YOU FAV LANGUAGE   ")

g=input("FOURTH FRIEND ENTER YOUR NAME PLEASE   ")
h=input("FOURTH FRIEND ENTER YOU FAV LANGUAGE   ")

newdict={
    a:b,
    c:d,
    e:f,
    g:h
}
myDict.update(newdict)
print(myDict)