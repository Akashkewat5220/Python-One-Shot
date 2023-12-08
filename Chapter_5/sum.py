def summation(n):
    
    if n == 1:
        return 1

    ans = n + summation(n-1)
    return ans

n = int(input("Enter value of n: "))
print(summation(n))
    