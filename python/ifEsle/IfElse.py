#comparrison operators
#== equal to, != Not equal to, < less than, > more than, <= lessthan equal to, >= more than equal to.


#Boolean operators And, not, or,  
#AND  → both must be true
#OR   → one must be true 
#NOT  → flips the value
#not and or The 3-second rule programmers use, Evaluate comparisons first ,Apply not, Apply and / or
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
username= "Aseel"
password= "Marlon"

if username == 'Aseel':
    print("Welcome Aseel")
else:
    print("invalid username")
if password == 'Marlon':
    print('password correct')
else:
    print("invalid password")
"""

name="Carol"
age=13
if name =="Alice":
    print ('Hello Alice')
elif age < 12:
    print('You are not Alice youngin')
elif age >100:
    print('you are not alice you granny')
elif age > 2000:
    print('you are not Alice you vampire')
else:
    print('we dont know who you are ngl')
