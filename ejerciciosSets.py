## Ejercicios de Sets

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

# Ejercicio 5: Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)  

# Ejercicio 6: Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)