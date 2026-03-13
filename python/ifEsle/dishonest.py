""" print('Enter  TB or GB for the adverstised unit')
unit = input('>')

if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)"""


"""
Write code that:

prints "Hello" if spam == 1

prints "Howdy" if spam == 2

prints "Greetings!" for anything else

Write the Python code. I'll grade it."""

spam =25

if spam==1:
    print('hello')
elif spam==2:
    print("Howdy")
else:
    print("Greetings")
