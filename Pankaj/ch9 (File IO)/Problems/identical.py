f1=open('copiedtext')
f2=open('Donket.txt')

f1read=f1.read()
f2read=f2.read()

if f1read==f2read:
    print("Yes the files are identical")
else:
    print("No,The files are not exectly same")