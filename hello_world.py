
#print("hello world")
#Variables
#- Used to store any data / user date
#-anything in quotation marks is a string
#-any number is a integer
#-yes or no is Boolean
#-if you have a number with a decimal it is a float

#How to find out the type of data stored
#-type()
#-print(type(variable name))

# - comment
# comment multiple lines at once ctrl + /

#first_name = "Mohamed"
#last_name = "Osman"
#DOB = "05/05/1998"
#Course_name = "Eng130"


print("Hello, What is your name")
first_name = input() # Takes the input from the user and stores in the variable
print("Please enter your last name")
last_name = input() # Takes the input from the user and stores in the variable
print("Nice to meet you", first_name, last_name)

print("What is your date of birth")
DOB = input()

print("What is your door number")
door_number = input()

print("What is the first line of your address")
address = input()

print("What are your hobbies?")
hobbies = input()


print("Nice to meet you, below are your details")
print("First name:" , first_name)
print("Last name", last_name)
print("D.O.B;", DOB)
print(f"Address: {door_number} {address}")
print("Hobbies", hobbies)