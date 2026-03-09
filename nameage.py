'''file says Hello, asks for name, it is good to meet you (name), 
prints the length of the name),asks for age,
 and prints how old u will be in 5 years.)'''
'''psuedo
first print the words hello 
then print a string that asks for the name 
then get the input from the user
then reply with its good to meet u with their input
then say your length of your name is 
and lastly how old theyll be in 5 years
'''

#print ('Hello')
#print ("What is your name?")
#user_name = input ("type your name here:")
#print ("its a pleasure to meet you, " + user_name)
#print (f"the length of your name is {len(user_name)}")
#user_age = input("enter your age:")
#print (f"In five years your age will be {int(user_age) + 5}")

#creates item variable
item = "cheese"
#sets the price
price = 2.5
#sets quantity
quantity = 7
# the total price is quantity times the price 
total = price * quantity 

#fstring prints the price of however many cheeses and the total is .2f is ex 2.00 .00 is .2f
print(f"The price for {quantity} {item}s comes out to ${total:.2f}")
print(f"The price of a one {item} is ${price}")