
### Operators
Data types and operators

Data types
```python
- subtract
+ add
* multiply
/ divide
```

Operators
```python
- < less than
-> greater than
== is equal to
>= greater than or equal to
<= less than or equal to
% modulus - takes remainder
!= not equal to 

a = 12
b = 23

print(a+b)
print(a-b)

comparison

print(a<b)
print(a==b)
```

## Boolean builtin methods in python
```python
greeting = ("Hello World")
print(greeting)
print(greeting.isalpha())  # is the string all alphabets
print(greeting.islower())  # is the string lowercase
print(greeting.startswith("H"))  # does the string start with the letter H
print(greeting.endswith("d"))  # does the string end with the letter d
print(greeting.isdigit())  # is the string all digits

string indexing - starts from 0]
H e l l o W o r l d !
1 2 3 4 5 6 7 8 9 10 11
print(greeting[5:2])  #- prints charachters 0 - 5
print(greeting[6:12]) #- prints characters 6 - 11

space = "lots of spaces at the end            "
print(len(space)) # prints length on string
print(len(space.strip())) #strip removes empty spaces at the end of a string

example_text = "Here is some work i wrote here today"
print(example_text.count("Here")) #counts number of times specified word is repeated
print(example_text.lower()) # makes all text lower case
print(example_text.upper()) # makes all text upper case
print(example_text.capitalize()) # makes first letter capital
print(example_text.replace("some", "hello")) # replaces the words specified
```


Data collections
- Lists
- Tuples
- Dict

Lists
```python
A list can have multiple data types, string, int etc
syntax list_name = ["freve", "vrebver", "dndnd"]

shopping_list = ["ketchup", "fanta", "eggs", "bread"]
print(shopping_list)
print(type(shopping_list))
How to add to a list
shopping_list.append("chicken")
print(shopping_list[3]) # prints the value in index 3
shopping_list[2] = "ice cream" # replaces in the list
print(shopping_list)
shopping_list.pop()
print(shopping_list) #deletes the last item in the list
shopping_list.remove("fanta") # removes from the list
print(shopping_list)
```

Tuples
```python
Cannot be changes, added to or edited
such as user details, DOB, etc
essentials = ("milk", "water")
print(essentials)
print(type(essentials))
essentials [0] = "coffee" # will not run - cannot edit a tuple
print(essentials)
```
Dict
```python
syntax = {"name": "sparta"}
         {   }... and so on
store student data: name, course_name, progress, completed_lessons
student_1 = {
    "keys": "values",
    "name": "Mohamed",
    "Course_name": "Eng130",
    "progress": "Good",
    "completed_tasks": "4",
    "completed_lessons": ["lists", "tuples", "operators"]
}
print(type(student_1))                       # prints type
print(student_1["name"])                     # prints the value of stated key
print(student_1)                             # prints dictionary
print(student_1["completed_lessons"])
print(student_1["completed_lessons"][0])

student_1["completed_tasks"] = 2            #changes value of completed tasks
print(student_1["completed_tasks"])

student_1["completed_lessons"][2] = "OOP"   # changes index 2 value
print(student_1["completed_lessons"])

How to delete an item from the list
student_1["completed_lessons"].remove("OOP") #deletes value
print(student_1["completed_lessons"])

How to display only keys or values
print(student_1.keys())
print(student_1.values())
```