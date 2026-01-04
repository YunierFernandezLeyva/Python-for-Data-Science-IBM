'''temp= [6,9,3,3,3,5,7,7]
def promedio(lista):
    return sum(lista)/len(lista)

print(promedio(temp))

for i in range(len(temp)):
    if temp[i] > promedio(temp):
        print(f"El valor {temp[i]} en la posición {i} es mayor al promedio")
'''

'''temp = [6, 9, 3, 3, 3, 5, 7, 7]

A = temp[0]
B = temp[-1]
print(A, B)
suma = sum(temp)/len(temp)
print(suma)'''

# Ejercicio 1: Cast the following list to a set:
['A','B','C','A','B','C']
set(['A','B','C','A','B','C'])

# Ejercicio 2: Add the string 'D' to the set S.
S = set(['A','B','C'])
S={'A','B','C'}
S.add('D')
print(S)

# Ejercicio 3: Find the intersection of set A and B.

A={1,2,3,4,5}
B={1,3,9, 12}
C = A & B
print(C)

# Ejercicio 4:  Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1
print(set1)