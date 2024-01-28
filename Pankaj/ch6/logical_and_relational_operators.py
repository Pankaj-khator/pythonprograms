age=int(input("Enter your age    "))
if(age>=18 and age<=30):
    print("You are eligible to work")
    print("ROUND 2")
    graduationmarks=int(input("Enter your graduation marks percentage    "))
    exp=int(input("Enter your experiance in years    "))
    if(graduationmarks>=60 or exp>=3):
        print("You are eligible to work")
    else:
      print("'SORRY' You are not eligible to work")
else:
     print("You are not eligible to work")


