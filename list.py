# The list is one of Python's main ordered collections.

# This line of code creates an empty list.
nums = []
print(nums)

# This line of code creates a list of 5 integers.
nums = [1, 2, 3, 4, 5]
print(nums)


# These lines of code are accessing an element value in
# the list by using its index. 
print(nums[1])
nums[4] = 6
print(nums)

# if an attempt is made to access an element outside of the 
# bounds of the list an IndexError will be thrown
# print(nums[5])
# nums[-6] = 0

# We may use negative indices in the square brackets.
# In the case of this list, -5, -4 , -3, -2, -1 are the 
# only valid indices, with -1 being the index for the last
# element and -5 being the index for the first element.
print(nums[-1])
print(nums[-5])

# The python len function tells us the number of elemts in a list.

print(len(nums))

# This line of code is creating a list of values of mixed types.
mixed = [1, 'one' , 2, 'two', 3, 'three']
print(mixed)

# A handy way to step through the elements in a list is by using a loop

# While loop

i = 0

while(i < len(nums)):
    print(nums[i], end=" ")
    i = i + 1
print()

# 5. Rewrite the while loop above so that it outputs only the nums
# that are less than 6.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0

while(i < 6):
    print(nums[i], end=" ")
    i = i + 1
print()

 

# Python has inbuilt functions that may be used to manipulate lists.

# The append function may be used to add one element at a time to a list.
names = []
print(names)

# These lines of code will use the append function to add elements one at a time
# to the list.
names.append('Sammy')
names.append('Mia')
names.append('Dean')
names.append('Copper')
print(names, '- original list')


# These lines of code addd multiple elements to list using a loop.
for i in range(1,5):
    names.append(i)
    print(names, 'i - add multiple elements using a loop')

# This line of code adds a Tuple to list.
names.append(('Chessie', 'Lexi'))
print(names, '- add Tuple')

# This line of code adds a Tuple to list.
names.append([1,2])
print(names, '- add list')

# The insert function may be used to add elements at a desired position in a list.
names.insert(0, 'Pixie')
names.insert(5, 0)
print(names, ' - insert function')

# The extend function may be used to add multiple elements to the end of a list. 
names.extend(['Lea', 'Fritz', 'Lea'])
print(names, '- extend function')

# Only the first occurence of the value will be removed from the list
names.remove('Lea')
print(names, '- remove function first value only')


# The remove function only removes one element at a time.
# To remove a range of eleements, a loop must be used.
names.reverse()
print(names)

for i in range(0, 5):
    names.remove(i)
    print(names, '- remove function range')

# The pop function can also be used to remove and return an element from a list.
last = names.pop()
print(last)
print(names , '- pop function')


# To remove an element from a sepcific position of a list, the index of the element
# may be passed as an argument to the pop function.
first = names.pop(0)
print(first)
print(names, '- pop funcion with index')