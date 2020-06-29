# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [25, 25, 50]
r = my_list[0] + my_list[1] + my_list[2]
print(r)

# Create a tuple, called my_tuple, with a single value in it
my_tuple = ('a',)
print(len(my_tuple))

'''
    --> When generating a one-element tuple, if you write only one object in parentheses (), the parentheses () are ignored and not considered a tuple.
    --> To generate a one-element tuple, a comma , is required at the end.
    --> If you just you () --> python thinks is for mathematical ()
    --> also can assign tuple without () --> 'a', --> python will understand its a tuple
'''

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12, 1}
result = set1.intersection(set2)
print(result)
