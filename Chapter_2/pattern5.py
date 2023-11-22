n = int(input("Enter n: "))

for i in range(n+1):
    for j in range(1 , i+1):
        print(chr(j + 64), end=" ")
    print()