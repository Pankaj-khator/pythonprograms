sub1 =float(input("Enter marks of subject 1 out of 100   "))
sub2 =float(input("Enter marks of subject 2 out of 100   "))
sub3 =float(input("Enter marks of subject 3 out of 100   "))
sub4 =float(input("Enter marks of subject 4 out of 100   "))

if(((sub1+sub2+sub3+sub4)/4)>40 and sub4>33 and sub3>33 and sub2>33 and sub1>33):
    print("the student is pass")
else:
    print("the student is fail")
