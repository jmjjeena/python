friends = {"Bob", "Matt", "Tom"}
abroad = {"Bob", "Tom"}

local_friends = friends.difference(abroad)
'''
Notes:
    --> x.difference(y) takes in another set
    --> it will take x set and remove y set from it
'''
print(local_friends)
# set() --> empty set

total_friends = friends.union(abroad)
'''
Notes:
    --> .union()
    --> unites 2 sets and gives you the total of the both
'''
print(total_friends)

art = {'Bob', 'Matt', 'Tom', 'Don'}
science = {'Bob', 'Matt', 'Sam', 'Jen'}
'''
Notes:
    --> Intersection of two given sets A and B is a set which consists of all the elements which are common to both A and B.
'''
both = art.intersection(science)
print(both)
