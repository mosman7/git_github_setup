# Data types and operators
# - subtract
# + add
# * multiply
# / divide
# Operators
# - < less than
# -> greater than
# == is equal to
# >= greater than or equal to
# <= less than or equal to

# a = 12
# b = 23
#
# print(a+b)
# print(a-b)
#
# comparison
#
# print(a<b)
# print(a==b)

# #Boolean builtin methods in python
# greeting = ("Hello World")
# print(greeting)
# print(greeting.isalpha())  # is the string all alphabets
# print(greeting.islower())  # is the string lowercase
# print(greeting.startswith("H"))  # does the string start with the letter H
# print(greeting.endswith("d"))  # does the string end with the letter d
# print(greeting.isdigit())  # is the string all digits



#
# greeting = "Hello World"
# print(greeting[5:2])  #- prints charachters 0 - 5
# print(greeting[6:12]) #- prints characters 6 - 11
#
# space = "lots of spaces at the end            "
# print(len(space)) # prints length on string
# print(len(space.strip())) #strip removes empty spaces at the end of a string
#
# example_text = "Here is some work i wrote here today"
# print(example_text.count("Here")) #counts number of times specified word is repeated
# print(example_text.lower()) # makes all text lower case
# print(example_text.upper()) # makes all text upper case
# print(example_text.capitalize()) # makes first letter capital
# print(example_text.replace("some", "hello")) # replaces the words specified


first_name = "Mohamed"
last_name = "Osman"
salary = 40

print(first_name)
print(last_name)
print(first_name, last_name)
print(first_name + " " + last_name, salary) # use a comma to combine int and string
print(f"Hello {first_name} {last_name} {salary}") # f string allows you to combine different variables together