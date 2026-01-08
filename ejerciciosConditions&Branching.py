#---------------------------------Comparison Operations--------------------------------#

'''
Comparison operations compare some value or operand and based on a condition, produce a Boolean. 
When comparing two values you can use these operators:

equal: ==
not equal: !=
greater than: >
less than: <
greater than or equal to: >=
less than or equal to: <=
'''

#Find the value of i that produces a True:
i=1
i!=0  # True
i==0  # False

#---------------------------------Branching--------------------------------#

#Find the value of x that prints the statement "this is a":

x="a"
if(x=='a'):
    print("this is a")
else:
    print("this is  not a")


# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")


# Else statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")


# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")


# Condition statement example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')


# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

#-------------------------------Logic Operators-------------------------------#

'''
and
or
not
'''

#Find the value of y that produces a True statement:

y=1
x=1
x>0 and y<10  # True

# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")


# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


    # Condition statement example

album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")