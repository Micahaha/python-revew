# Expressions in Python evaluate to true or false.
# Expressions use the comaparison operators: <,
# >, <=, >=, ==, != 

x = 4

print(x < 5)
print(x > 5)
print(x == 5)
print(x != 5)


# Python supports the if, if-else, if-elif-else, and 
# nested if decision structures

# the if decision structure tests its condition
# and if the condition is true, it executes the code
# block its given.

if (x < 5):
    print('x is less than 5 is true.')


# Here is the shorthand version of the if decision. 
if(x < 5): print('x is less than 5 is true.')

# The if-else decisison structure tests its condition
# and if the condition is true, it executes the code block
# it's given. If the condition is false, the coe block
# given to the else is executed. 
if (x==5): 
    print('x is equal to 5 is true. ')
else:
    print('x is equal to 5 is false. ')
    

# Here is the shorthand version of the if-else decision.
print('x is equal to 5 is true') if (x==5) else print('x is equal to 5 is false.')

# The if-elif-else decision structure tests multiple 
# conditions. The code block given to the condition that's 
# true is executed. If none of the conditions are true
# the code block given to the else is executed
if(x > 5):
    print('x is equal to 5 is true.')
elif (x==5):
    print('x is equal to 5 is true.')
elif(x < 5):
    print('x is less than 5 is true.')
elif(x != 5):
    print('x is not equal to 5 is true')
else:
    print('None of the conditions is true.')


# A nested if decision is an if statement that is the target
# of another if statement. 
if(x < 5):
    print('x is less than 5 is true.')
    if(x != 5):
        print('x is not equal to 5  is true. ')

    
# Comparison operators may be chained together.
a = 5
b = 10
c = 15

if a < b < c:
    print('b is greater then a and less than c.')



grade = 'A'

match grade:
    case 'A':
        print('Super work!')
    case 'B':
        print('Good job!')
    case 'C':
        print('You made it.')
    case 'D', 'F':
        print('Oh, Dear...')
    case _:
        print('Invalid Grade')

# Python supports the ternary operator. 

result = 'x is equal to 5 is true' if (x==5) else 'x is equal to 5 is false.'
print(result)
print('x is equal to 5 is true.' if (x==5) else 'x is equal to 5 is false')


# The ternary operator may be written using tuples.
# (false value, true value) [expression to test]
# x = 5
result = ( 'x is equal to 5 is false.', 'x is equal to 5 is true.') [x==5]
print(result)

# The ternary operator may be written using dictionaries.
result = {True: 'x is equal to 5 is true.', False: 'x is equal to 5 is false'} [x == 5]
print(result)


# Expressions in python may also use the logical operators:
# and, or and not.
num = 50

# This if-else decision structure tests if num is between 1 and 100.
if (num >= 1 and num <= 100):
    print('num is between 1 and 100.')
else:
    print('num is not between 1 and 100')


if (num < 1 or num > 100):
    print('num is not between 1 and 100')
else:
    print('num is between 1 and 100')


foundIt = False

if (not foundIt):
    print('FoundIt is false.')
else:
    print('FoundIt is true.')

# It requires Python 3.10 or newer. 

grade = 'Z'

match grade:
    case 'A':
        print('Super work!')
    case 'B':
        print('Good job!')
    case 'C':
        print('You made it.')
    case 'D', 'F':
        print('Oh, Dear...')
    case _:
        print('Invalid Grade')


# 3. Rewrite the match-case decision structure above as an if-elif-else
# decision structure.

if grade == 'A':
    print('Super work!') 
elif grade == 'B':
    print('Good job!')
elif grade == 'C':
    print('You made it.')
elif grade == 'D' or grade == 'F':
    print('Oh, dear ... ')
else:
    print('Invalid Grade')

