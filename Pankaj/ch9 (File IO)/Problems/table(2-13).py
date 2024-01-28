import os
print(os.listdir())
xyz = str(input("copy path of any folder in your pc and paste it here "))
os.chdir(xyz)
print(os.listdir())
x=int(input("Enter a number from that you want tables  "))
y=int(input("Enter a number till that you want tables  "))

choice = int(input('''Press 1 if you want in one text file \n Press 2 if you want in different text file '''))


if choice ==1:
 for a in range (x,y):
          
          tb = open('Table of '+str(a),'w')
          tb.close()
  
 for a in range(x,y):
    for b in range (11):
          tb = open('Table of '+str(a),'a')
          unknown  = a,'*' ,b,'=',a*b
          tb.write(str(unknown))
          tb.write("\n")
          tb.close()
elif choice ==2 :
 tb = open('Table ','w')
 tb.close()
 for a in range(x,y):
    for b in range (11):
          tb = open('Table of '+str(a),'a')
          unknown  = a,'*' ,b,'=',a*b
          tb.write(str(unknown))
          tb.write("\n")
          tb.close()
else:
    print("Invaild input")