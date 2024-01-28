f = open('sample.txt','r') # 'rb' to open in binary and 'r' or 'rt' as text 
data = f.read()
print(data)


data = f.readline() #read first line
print(data)

data = f.readline() #read second line
print(data)

data = f.readline() #read third line
print(data)

f.close()
# import os
# print(os.listdir())