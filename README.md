# Python 

## Why Python
- Python has recently become one of the mos popular programming languages in the world. Python is very easy to learn due to its simplified syntaxes and versatility hence can be used by all people ranging from top level developers to those new to tech who arent tech savvy.

## Python use cases
In addition to being easy to learn the language is also very versatile, Python is used in all sorts of fields including 
- Machine learning
- Artificial intelligence
- Data science
- Game development
- Web development
- Hardware programming
- and much more
#### Python Variables
Variables are used to store data
- Anything in quotation marks is a string
- Any number is a integer
- Yes or no answers are Boolean
- If you have a number with a decimal it is a float

How to find out the type of data stored
- type()
- print(type(variable name))

How to comment multiple lines at once ctrl + /

`print ("Hello World")`
``` python
first_name = "Mohamed"
last_name = "Osman"
DOB = "05/05/1998"
Course_name = "Eng130"
uk_resident = bool


print("Hello, What is your name")
first_name = input()
print("Please enter your last name")
last_name = input()
print("Nice to meet you", first_name, last_name)
dgfgd
print("What is your date of birth")
DOB = input()

print("Are you a UK resident?")
uk_resident = input()
```

## Github setup
### Generating a new SSH key
- Open git bash admin
- Paste in the below text and sub in your email
```python
$ ssh-keygen -t ed25519 -C "your_email@example.com"
```
- When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.
- When prompted, type a secure passphrase and confirm

### Adding your SSH key to the ssh-agent
- In Git bash admin type:
```python
eval "$(ssh-agent -s)"
```
- This should return:
```python
Agent pid 59566
```
- Now add your SSH private key to the ssh-agent, if you created your key with a different name replace 'id_ed' with the name of your private key file.
```python
 ssh-add ~/.ssh/id_ed
```
- Now add the SSH key to your account on github

## Create a repository on GitHub and follow the below steps to connect github to pycharm

- git init
- git add .
- git commit -m "updated"
- git branch -M main
- git remote add origin "git@github.com:[username]/[repository].git"
- git push -u origin main

#### Git & GitHub
How to add changes to github repo from localhost
- If you are unsure what changes you made:
- git status
- git add . / git add filename
- this pushes any changes made current location
- git commit -m "updated"
- git push -u origin main

Making changes to localhost from github
- git pull