#creates item variable
item = "cheese"
#sets the price
price = 2.5
#sets quantity
quantity = 7
#the total price is quantity times the price 
total = price * quantity 

#fstring prints the price of however many cheeses and the total is .2f is ex 2.00 .00 is .2f
print(f"The price for {quantity} {item}s comes out to ${total:.2f}")
print(f"The price of a one {item} is ${price}")