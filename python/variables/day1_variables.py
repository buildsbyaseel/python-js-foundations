''' Just day 1 python refresh '''
#expression = 2 + 3 or 3 / 1
#2,3  3,1 are the values

# % is the modulus operator which gives you the remainder of the division of the numbers
print (14 % 3)

# / division regualar returns 4.5
print(9/2)

# // this is the division of the numbers but gives it rounded down to the nearest whole number
print (14 // 4)

# * is multiplication
print (14 * 4)

# + is addition
print (14 + 4)

# - is subtraction
print (14 - 4)

# ** is exponentiation or exponent operator basically 2 to the power of 3 which is 2*2*2
print (2 ** 3)

#order of operations is (), exponents, *, / (w remainder), //, +, last -

#can add strings/ word "concatenation
print ("4" + "2")

print ("aseel" + "malik")

print (4 + 2)

#string replcation multiplies string aseelaseelaseelaseelaseel
print ("aseel" * 5)

#variables
spam = 42
eggs = 2 
print (spam + spam + eggs)
#overwrite the variable now spam is 44
spam = spam + 2
print (spam)

#cant concatonate a striaght up int in a print have to convert it into a string 
age=25
print ("I am " + str(age) + " years old")

int(12.6)
#= 12 rounds down

float(23)
#23.0

#type function returns int tells u what type of data int str float boolean
type(23)

#round() and abs() functions
round(3.13) #returns 3 rounds to the neartes whole buttttt
round(2.5)#rounds to 2 because if its .5 it rounds to the even number so
round(3.5)#rounds to 4 becuase its the closest even 
#can round to the nearest anything
round(2.32232,2) # returns 2.2

#abs function absoulte value of a number or positve value
abs(-23)# returns 23
abs(23)# returns 23

#binary 128 64 32 16 8 4 2 1  / byte = 8 bits -01010101  
#   1 byte = 8 bits     1 KB = 1024 bytes     1 MB = 1024 KB     1 GB = 1024 MB

#boolean values true and false

#comparrison operators
#== equal to, != Not equal to, < less than, > more than, <= lessthan equal to, >= more than equal to.