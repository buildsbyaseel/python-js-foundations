import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')
print('Done')



#in debugger under watch if alot of variables u can type what u want and it will pin it to the top 


'''Continue: Runs the program normally until it hits the next breakpoint.

Step Into: Digs deeper. If the current line is a function call, the debugger goes inside that function so you can see its code.

Step Over: This is the "Safe Step." It executes the current line and moves to the next one in the same file. If that line is a function, it runs the function at full speed and just shows you the result.

Step Out: The "Get me out of here" button. It finishes the current function and takes you back to the line that called it.

Stop: Immediately kills the program.'''
