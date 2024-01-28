poem = open("poems.txt",'r')
readpoem = poem.read()
print(readpoem   )
a="twinkle"

if a in readpoem:
    print("\nYes the file contain the word " , a , readpoem.count(a) ,"times")
    
else:
    print("no")
poem.close()