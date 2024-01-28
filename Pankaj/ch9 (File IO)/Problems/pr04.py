file = open('Donket.txt','r')
string = file.read()
file.close()

file = open('Donket.txt','w')
for Donkey in string:
 string = string.replace('Donkey', '######')
file.write(string)
 
# print(string)
file.close()