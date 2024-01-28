list=[1,'donkey','o',23,34,'donkey',90.1]
print(list)
Llen=len(list)
# print(Llen)
for i in range(Llen):
    if list[i] == "donkey":
       list[i] = "@#$%^&^%"
    else:
      pass
  

print(list)