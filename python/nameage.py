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

print('Hello')

user_name = input("What is your name?:")

print(f"its a pleasure to meet you, {user_name}")
print(f"the length of your name is {len(user_name)}")

user_age = int (input("enter your age:"))

print(f"In five years your age will be {user_age + 5}")



