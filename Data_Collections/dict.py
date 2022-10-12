# Dictionary - data collection type
#syntax = {"name": "sparta"}
#         {   }... and so on
# store student data: name, course_name, progress, completed_lessons
student_1 = {
#   "keys": "values"
    "name": "Mohamed",
    "Course_name": "Eng130",
    "progress": "Good",
    "completed_tasks": "4",
    "completed_lessons": ["lists", "tuples", "operators"]
}
print(type(student_1))                  # prints type
print(student_1["name"])                # prints the value of stated key
print(student_1)                        # prints dictionary
print(student_1["completed_lessons"])
print(student_1["completed_lessons"][0])

student_1["completed_tasks"] = 2            #changes value of completed tasks
print(student_1["completed_tasks"])

student_1["completed_lessons"][2] = "OOP"   # changes index 2 value
print(student_1["completed_lessons"])

# delete an item from the list
student_1["completed_lessons"].remove("OOP") #deletes value
print(student_1["completed_lessons"])

#dict builtin methods
# can display only keys or values
print(student_1.keys())


# Dictionary basics :D

#1 - Define a dictionary call story1, it should have the followign keys:
        # 'start', 'middle' and 'end'

story1 = {
    "start": "I was in the shopping centre and i met a beautiful lady",
    "middle": "we spoke and had a coffee date",
    "end": "we got married and lived happily ever after"
}

#2 - Print the entire dictionary
print(story1)

#3 - Print the type of your dictionary
print(type(story1))

#4 - Print only the keys
print(story1.keys())

#5 - print only the values
print(story1.values())

#6 - print the individual values using the keys (individually, lots of printi commands)
print(story1["start"])
print(story1["middle"])
print(story1["end"])

#7 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero

story1["hero"]= "Angel"
print(story1)