# pass by value is for immutable objects

#when passed in function only copy of the object is created and assigned to local variable in functio
# Any change made to them in side function , do no t affect the original variabale outside function

#PASS BY VALUE

def addOne(x):
    x = x + 1 
    print("Inside functio:" , x)

x = 5 
addOne(x)
print("Value at outside of the function:" , x)

#pass aby reference = we pass mutable objects like list and dictionary
#Actual object is passedto the function
# Changes inside the function will effect the original object

def modifyList(lst):
    lst.append(4)
    print(lst)

lst = [1,2,3,45]
output = modifyList(lst)
print(output)