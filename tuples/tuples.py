# Creating a tuple
my_tuple = ('apple', 'banana', 'cherry')

# Accessing an item
print(my_tuple[0])  
print(my_tuple[-1]) 

# Adding an item to the tuple
my_tuple = my_tuple + ('date',)
print(my_tuple)


# Removing an item from the tuple
my_tuple = my_tuple[:1] + my_tuple[2:]
print(my_tuple) 