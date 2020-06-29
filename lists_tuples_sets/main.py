# 3 different collections
# lists
l = ["Bob", "John", "Matt"]
# tuple
t = ("Bob", "John", "Matt")

'''
Difference between a list and a tuple
    --> you can't modify a tuple
    --> where as you can add and remove items from a list but not in tuple
'''

# set
s = {"Bob", "John", "Matt"}

'''
Difference between set and the other two
    --> You add and remove from set but you cant have duplicate elements
    --> can't have Bob twice
    --> lists and tuples keeps the order of the elements
    --> whenever you print out the list it will print out in the same order as it was stored
    --> but sets won't keep the order
    --> has {} 
    --> You can't access individual elements of a set by using subscript notation
'''

'''
Notes:
    --> You can access individual elements of a list or a tuple by using subscript notation
'''
print(l[0])
print(t[2])

# modify a list
l[0] = "Mike"
print(l)

# add to a list
l.append("Jerry")
print(l)

# remove from a list
l.remove("Mike")
print(l)

#  add to a set
'''
Notes:
    --> it's add not append when it comes to sets.
    --> append means to add to the end but sets doesn't have end
'''
s.add("Smith")
s.add("Smith")
print(s)
# no duplicates has been added
