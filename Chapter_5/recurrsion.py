def factorial(n):

    #base case conditon
    if n== 0:
        return 1
    
    #recurssive case
    ans = n * factorial(n-1)
    return ans


n = int(input("Enter value of n: "))
print(factorial(n))