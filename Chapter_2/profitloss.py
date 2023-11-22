cost_price = int(input("Enter the cost price:"))
selling_price = int (input("Enter the selling price:"))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("We have made profit of: " , profit)
    profit = selling_price - cost_price
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("We have made loss of: " ,loss)
else:
    print("We have made no profit and no loss")