
#--------------------------------Dictionary Methods--------------------------------#

# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print("Original Dictionary:", Dict)

# Access to the value by the key
Dict["key1"]

# Access to the value by the key
Dict[(0, 1)]

# Create a sample dictionary
# Each key is separated from its value by a colon ":". 
# Commas separate the items, and the whole dictionary is enclosed in curly braces. 
# An empty dictionary without any items is written with just two curly braces, like this "{}".

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print("\nSample Dictionary:", release_year_dict)

# Get value by keys
release_year_dict['Thriller'] 

# Get all the keys in dictionary
release_year_dict.keys() 

# Get all the values in dictionary
release_year_dict.values() 

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
print("\nDictionary after adding Graduation:", release_year_dict)

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print("\nDictionary after deleting Thriller and Graduation:", release_year_dict)

# Verify the key is in the dictionary
'The Bodyguard' in release_year_dict
print("\nIs 'The Bodyguard' in the dictionary?", 'The Bodyguard' in release_year_dict)

#--------------------------------Quiz on Dictionaries--------------------------------#

# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}

# In the dictionary soundtrack_dic what are the keys ?
soundtrack_dic.keys()
print("\nKeys in soundtrack_dic:", soundtrack_dic.keys())   

#b) In the dictionary soundtrack_dic what are the values ?
soundtrack_dic.values()
print("\nValues in soundtrack_dic:", soundtrack_dic.values())  

#--------------------------------Exercise on Dictionaries--------------------------------#

#a) Create a dictionary album_sales_dict where the keys 

'''are the album name and the sales in millions are the values.
The Albums Back in Black, The Bodyguard and 
 Thriller have the following music recording sales in millions 50, 50 and 65 respectively:'''

album_sales_dict = {"Back in Black": 50, "The Bodyguard": 50, "Thriller": 65}  

#b) Use the dictionary to find the total sales of Thriller:
print("\nSales of Thriller:", album_sales_dict["Thriller"], "million")

#c) Find the names of the albums from the dictionary using the method keys():
print("\nAlbum names:", album_sales_dict.keys())    

#d) Find the sales of the albums from the dictionary using the method values():
print("\nAlbum sales in millions:", album_sales_dict.values())  

#--------------------------------Scenario:Inventory Store--------------------------------#

#First you need to create an empty dictionary, where you will be storing the product details.