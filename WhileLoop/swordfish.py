#learn continue statements
#while true; run the loop indefinatly until its not true 
while True:

    print("who are you?")
    name = input ('>')#name variable input
    if name != "Joe":    #if name is not joe then 
        continue #continue means to start the loop over

    while True:  #nested loop so we dont have to go back into the whole entire steps again if password is wrong 
        print('Hello Joe, what is the password(its a fish)')

        password=input('>')
        if password == ('Swordfish'):
            break #breaks the password loop 
        else:
            print("wrong password try again")
    break #breaks from the who are you loop
print('access granted')
