import os
print("Press enter after every task")
xyz = str(input("copy path of any folder in your pc and paste it here "))
os.chdir(xyz)
print(os.listdir())
x=int(input("Enter a number from 0 to 10  "))
y=int(input("Enter a highest number less than 50000  "))
name=str(input("Enter your name  "))
choice = int(input('''Press 1 for surprize  '''))
if choice==2:
    tb = open('Hum_:-','w')
    tb.close()


if choice ==1:
 for a in range (x,y):
          tb = open('fuddu '+ name +str(a),'w')
          tb.close()
  
 for a in range(x,y):
    for b in range (1000):
          tb = open('Fuddu '+ name +str(a),'a')
          unknown  = "I LOVE YOU"+ str(b)
          tb.write(str(unknown))
          tb.write("\n")
          tb.close()
elif choice ==2 :
 for a in range(x,y):
    # for b in range (110):
          tb = open('Hum_:-)','a')
          unknown  = "I LOVE YOU "+ str(a)
          tb.write(str(unknown))
          tb.write("\n")
          tb.close()
else:
    print("you not deserve surprize")
    exit()