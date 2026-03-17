#while loop while true is like a infinite loop an u gotta break to exit 
"""
while loop has these steps
1. while
2. a condition that evalutes to true or false
3. a colon:
4. the block """

"""
while True:
    username=input("type your username:")

    if not username.isalpha():
        print("error: username must contain only alphabets")
    else: 
        break
    
password= input("type your password:")

print (f'Login Successful. Welcome {username}.')
"""

"""
spam=0

while spam<5:
    spam=spam + 1
    print("hello")
"""

#annoying whle loop  asks to type your name
"""
name =''
while name != 'your name':
    print('please type your name')
    name = input('>')
print ('thank you')
"""

while True:
    name = input('Type your name here: ')
    if name == 'your name':
        break
print('thanks')