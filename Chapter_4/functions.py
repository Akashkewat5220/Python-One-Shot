# n = int(input("Enter n:"))

# sum = 0
# for i in range(1 , n+1):
#     sum = sum + i

# print("Required sum will be:", sum)

# n1 = int (input("enter another n:")) ##another code to do the same task:

# sum1 = 0
# for i in range(1 , n+1):
#     sum1 = sum1 + i


## Functions = block of code ehich we can reuse again and again. Takes input and give the output
## syntax
##def funtion name (parameters)

## function callilng 
## function name (arguement1 , arguemesnst2)

# function def

# def printHello():
#     ## functio ki body
#     print("Hello world!!")

# printHello()

# function taking 2 number and returning the sum
def add (n1 = 8 , n2 = 9):
    sum = n1 + n2
    return sum

# //positional arguements
# print(add(2 , 3))

# //keyword arguement
# print(add(n1  = 2 ,n2 =  3))

#default arguemetn
# print(add())

#use of the args

# in args we can pass many arguements

# def addAllNumber(*args):
#     sum = 0 
#     for i in args:
#         sum+=i
#     return sum
# output = addAllNumber(1,2,3,4,5,6)
# print(output)

## USE OF KWARGS
# def studentInfo(**kwargs):
#     for x , y in kwargs.items():
#         print(x , y)

# studentInfo(name = 'Akash' , age = 20 , city = 'Pune')

#WRITING A FUNCTION FOR CALCULATING SUM FROM 1 TO N
def sumOneToN(n):
    sum = 0
    for i in range(1 , n):
        sum+=i
    return sum

n = int(input('Enter the input'))
#call function
output = sumOneToN(n)
print(output)