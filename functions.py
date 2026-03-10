# First function example: Add 1 to a and store as b


from typing import Dict


def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

# Get a help on add function

help(add)

# Call the function add()

add(1)

# Call the function add()

add(2)

# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

# Use mult() multiply two integers

Mult(2, 3)

# Use mult() multiply two floats

Mult(10.0, 3.14)

# Use mult() multiply two different type values together

Mult(2, "The BodyGuard ")


# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

# Initializes Global variable  

x = 3
# Makes function call and return function a y
y = square(x)
y

# Directly enter a number as parameter

square(2)

# Function example

def type_of_album(album, year_released):
    
    print(album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("The BodyGuard", 1980)
print(x)



#-------------------------------------Quiz on Functions---------------------------------

#Come up with a function that divides the first input by the second input:
def divide(num1, num2):
    result = num1 / num2
    return result

#Use the function con for the following question.
def con(a, b):
    return (a + b)

#Can the con function we defined before be used to add two integers or strings?
#Yes, the con function can be used to add both integers and strings.
print(con(2, 3))          # Adding two integers
print(con("Hello, ", "World!"))  # Adding two strings   


#Can the con function we defined before be used to concatenate lists or tuples?
#Yes, the con function can be used to concatenate both lists and tuples.
print(con([1, 2], [3, 4]))      # Concatenating two lists
print(con((1, 2), (3, 4)))      # Concatenating two tuples


#Write a function code to find total count of word little in the given string: 
# "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.
# Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"**

def count(text,passedkey):
    words = []
    words = text.split()
    Dict = {}

    for key in words:
        if(key == passedkey):
            Dict[key] = words.count(key)
print("Total count",Dict)

count("Mary had a little lamb Little lamb, little lamb Mary had a little lamb. Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go", "little")