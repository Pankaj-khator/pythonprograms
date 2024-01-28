num=int(input("Enter a number  ->"))
prime=True
print(range(2,num))
for i in range(2,num):
    if(num%i==0):
          prime=False
          break
if prime==False:
  print(num,"is not a prime number")
else:
  print(num,"is a prime number")

