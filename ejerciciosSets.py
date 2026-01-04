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
print(album_set1.difference(album_set2))

# Use intersection method to find the intersection of album_list1 and album_list2
album_set1.intersection(album_set2) 
print(album_set1.intersection(album_set2))  

# Find the union of two sets
album_set1.union(album_set2)
print(album_set1.union(album_set2))

# Check if superset
set(album_set1).issuperset(album_set2)
print(set(album_set1).issuperset(album_set2)) 

# Check if subset
set(album_set2).issubset(album_set1)
print(set(album_set2).issubset(album_set1))   

# Check if subset
set({"Back in Black", "AC/DC"}).issubset(album_set1) 
print(set({"Back in Black", "AC/DC"}).issubset(album_set1))

# Check if superset
album_set1.issuperset({"Back in Black", "AC/DC"})   
print(album_set1.issuperset({"Back in Black", "AC/DC"}))

#---------------------------Quiz on Sets----------------------------------------

#Convert the list ['rap','house','electronic music', 'rap'] to a set:
set(['rap','house','electronic music','rap'])

#Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])   
sum(A) == sum(B)
print("La suma de A es" , sum(A))   
print("La suma de B es" , sum(B)) 
print(sum(A) == sum(B))

# Create a new set album_set3 that is the union of album_set1 and album_set2:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print(album_set3)

#Find out if album_set1 is a subset of album_set3:
album_set1.issubset(album_set3)
print(album_set1.issubset(album_set3))