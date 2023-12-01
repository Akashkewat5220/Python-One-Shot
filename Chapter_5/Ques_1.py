def printNto1(n):
    
    #base condition
    if n==0:
        return

    print(n)
    printNto1(n-1) 

n = int(input("Enter value of n: "))
print(printNto1(n))