def greatest():
    a = int(input("enter 1st number"))
    b = int(input("enter 2nd number"))
    c = int(input("enter 3rd number"))
    if(a>b and a>c):
        print(a," is the greatest number")
    elif(b>a and b>c):
        print(b," is the greatest number")
    else:
        print(c," is the gretest number")

greatest()