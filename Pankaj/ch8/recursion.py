# # iter
n =4 
product = 1
for i in range (n):
    product = product *(i+1)
print(product)


# #iter
def factorial_iter(n):
    product = 1
    for i in range (n):
       product = product *(i+1)
    return product
  
print(factorial_iter(6))

#recursion
def fact_recursive(n):
    if n ==1 or n==0:
        return 1
    return n * fact_recursive(n-1)
print(fact_recursive(5))