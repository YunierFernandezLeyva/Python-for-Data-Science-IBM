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

#---------------------------Set Operations---------------------------------------

# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

# Add element to set
A.add("NSYNC")
print(A) 

# Try to add duplicate element to the set
A.add("NSYNC")
print(A)

# Remove the element from set
A.remove("NSYNC")
print(A)

# Verify if the element is in the set
"AC/DC" in A
print("AC/DC" in A)

#---------------------------Sets Logic Operations--------------------------------

# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
print(album_set1, album_set2)

# Find the intersections
intersection = album_set1 & album_set2
print(intersection)

# Find the difference in set1 but not set2
album_set1.difference(album_set2)