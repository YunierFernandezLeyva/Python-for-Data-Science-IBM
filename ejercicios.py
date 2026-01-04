'''temp= [6,9,3,3,3,5,7,7]
def promedio(lista):
    return sum(lista)/len(lista)

print(promedio(temp))

for i in range(len(temp)):
    if temp[i] > promedio(temp):
        print(f"El valor {temp[i]} en la posición {i} es mayor al promedio")
'''

temp = [6, 9, 3, 3, 3, 5, 7, 7]

A = temp[0]
B = temp[-1]
print(A, B)
suma = sum(temp)
print(suma)