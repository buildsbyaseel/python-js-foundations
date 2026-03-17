"""“TRUTHY” AND “FALSEY” VALUES AND THE BOOL() FUNCTION

Conditions will consider some values in other data types equivalent to True or False. When used in conditions, 
0, 0.0, and '' (the empty string) are considered False, while all other values are considered True.
The "Rule of Thumb" """

"""Use Shorthand when you just want to know if a variable is "empty" or "not empty" (like a name).

Use Explicit (>=, ==) when the specific value of a number matters for your logic."""


name = ''  #name ='' its set to a blank string with makes it false 
while not name: #this is while name is true or when the user enters anything
    print('what is your name') 
    name = input('>') #gets the input for name 
print(f'Hello {name} how many guests will you have?')
num_of_guests = int (input('>')) #gets the input that has to be a int
if num_of_guests: #means if num_of guests is anything but false or blank it does the print
    print(f'make sure you have enough room for {num_of_guests} guests') 
print("done")