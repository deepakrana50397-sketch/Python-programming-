#   Name Assignment (Variables & Constants)
#   Programmers can bind names (also called variables) to any type of object using the assignment = operator: <name> = <value>. A name can be reassigned (or re-bound) to different values (different object types) over its lifetime:

first_variable = 1 

second_variable = " hi"


print(type (first_variable))
# <class 'int'> type is int 

print(type (second_variable))

#<class 'str'> type is str

first_variable = " i am the new one "
#You may re-bind a name to a different object type and value.

second_variable = 30000



print(type (first_variable))
#<class 'str'> type is str

print(type (second_variable))
# <class 'int'> type is int 
#<-- Strings can be declared using single or double quote marks.

# Constants are names meant to be assigned only once in a program — although Python will not prevent re-assignment. Using SCREAMING_SNAKE_CASE signals to anyone reading the code that the name should not be re-assigned, or its value mutated. Constants should be defined at a module (file) level, and are typically visible to all functions and classes in a program.


I_AM_A_CONSTANT = 19