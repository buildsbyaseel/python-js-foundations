#import the module logging
import logging

#kill switch to stop all the debug
#logging.disable(logging.CRITICAL)

logging.basicConfig(filename='programlog1.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') #change level to logging.ERROR for prod and user doesnt see anything it stops running 
logging.debug('start the program')

def factorial(n):
    logging.info(f'Start of factorial for input: ({n})')
    if n<0:
        logging.critical(f'user entered a negative number Math Logic Failing.')
        return None
    total = 1 
    for i in range (1, n + 1):
        total *= i 
        logging.debug (f'i is {i}, total is {total}')
    logging.info(f'End of factorial complete result is:({total})')
    return total

print(factorial(-2))
logging.debug('END of program')





"""
import tool
logging.basicConfig() is the control room u put everythingu want it to do inside
filename='myProgramLog.txt'= makes it print the stuff in the specified file
(level=logging.DEBUG = shows u the debug steps 
, format=' = 'how it looks in terminal or txt file
%(asctime)s = shows the time
Line %(lineno)d = prints line number 
- %(levelname)s = shows the level like its debugging
- %(message)s whatever u put in the strings in the program  inside of logging.debug('start of program')
"""











''' logging has levels of importance

DEBUG = detailed info usually only for fixing bugs mode.  priority 10

INFO = Confirmation that things are working (e.g., "User logged in").  priority 20 

WARNING = Something unexpected happened, but the app is still alive.   priority 30

ERROR = A major problem (like a database crash). The app might still run.   priority 40

CRITICAL = Total failure. The program is stopping now.   priority 50

'''

"""
#this is for if u wanted 3 seperate log files for each level 
import logging

# 1. Create a "Root" Logger (The Main Hub)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG) # Let everything through the hub first

# 2. Create the "Debug" Handler (Saves everything)
debug_handler = logging.FileHandler('all_details.log')
debug_handler.setLevel(logging.DEBUG)

# 3. Create the "Warning" Handler (Saves Warnings and up)
warn_handler = logging.FileHandler('warnings.log')
warn_handler.setLevel(logging.WARNING)

# 4. Create the "Critical" Handler (Saves ONLY the disasters)
crit_handler = logging.FileHandler('emergencies.log')
crit_handler.setLevel(logging.CRITICAL)

# 5. Add a Format (Optional, but makes them readable)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_handler.setFormatter(formatter)
warn_handler.setFormatter(formatter)
crit_handler.setFormatter(formatter)

# 6. Plug the handlers into the Hub
logger.addHandler(debug_handler)
logger.addHandler(warn_handler)
logger.addHandler(crit_handler)

# --- NOW TEST IT ---
logging.debug("This only goes to all_details.log")
logging.warning("This goes to all_details AND warnings.log")
logging.critical("THIS GOES TO ALL THREE FILES!")

"""