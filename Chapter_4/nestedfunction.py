#function inside a function is the nested function

def output_function():
    x = 1 

    def inner_function():
        y = 2 
        result = x + y
        return result
    
    return inner_function()

output = output_function()
print(output)