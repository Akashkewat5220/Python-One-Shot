# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))

# if num1 > num2 and num1 > num3 :
#     print("num1 is the greatest ")
# elif num2 > num1 and num2 >num3:
#     print("num2 is the greatest ")
# else:
#     print("num3 is the greatest")


n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
n3 = int(input("Enter num3: "))

if n1 > n2:
    if n1 > n3:
        print("n1 is the greatest")
    else:
        print("n3 is the greatest")
else:
    if n2 > n3:
        print("n2 is the greatest")
    else:
        print("n3 is the greatest")