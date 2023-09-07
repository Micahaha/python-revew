iterable = [9,8,7,6,5,4,3,2,1]

for i in iterable:
    print(i, end=" ")
print('blastoff!')



# Dictionary

iterable = dict({'nine':9,
                'eight':8,
                'seven':7,
                'six':6,
                'five':5,
                'four':4,
                'three':3,
                'two':2,
                'one':1})

for i in iterable:
    print("%d" % (iterable[i]), end=" ")
print('blastoff!')

# The while loop must be provided a condition.
# As long as the condition is true, its code
# block will be executed.

i = 9

while (i > 0):
    print(i, sep=" ", end=" ")
    i = i - 1
    # There must be a line of code in the code block
    # that forces the condition to become false, else
    # the loop will repeat infinitely.

print("blastoff!")


i = 9

while (i > 0):
    if(i % 2 == 0):
        print(i, sep=" ", end=" ")
    i = i - 1 

    # There must be a line of code in the code block
    # that forces the condition to become false, else
    # the loop will repeat infinitely.

print("blastoff!")





