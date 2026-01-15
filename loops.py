
##Use loops to print out the elements in the list A:
A=[3,4,5]
for element in A:
    print(element)

#Find the value of  x  that will print out the sequence  1,2,..,10 :
x=10
y=1
while(y != x):
    print(f"El valor de y es: {y}" )
    y=y+1


# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

#Example 1: Using break in a for loop

for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at:", num)
        break
    print(num)


#Example 2: Using continue in a for loop

for num in range(1, 6):
    if num == 3:
        continue
    print(num)  


#Example 3: Using break and continue in a while loop

count = 0
while count < 10:
    count += 1
    if count == 3:
        continue  # skip printing 3
    if count == 8:
        break     # stop the loop when count is 8
    print(count)


#---------------------------------Quiz on Loops---------------------------------

for i in range(-5, 5):
    print(f"El rango es {i}")


#Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']. 
# Make sure you follow Python conventions.

Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in Genres:
    print(f"Los géneros son {i}")


#Write a for loop that prints out the following 
# list: squares=['red', 'yellow', 'green', 'purple', 'blue']

squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in squares:
    print(f"Los colores son {i}")