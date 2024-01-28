def sum_of_n(n):
    # if n ==1 :
    #    return 1
    if n ==0 :
       return 0
    return n + sum_of_n(n-1)
print(sum_of_n(4))




