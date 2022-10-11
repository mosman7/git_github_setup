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
- git fetch
- git commit -m "new"
- git pull

```python
$ git
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

```

### Operators
Data types and operators
```python
Data types
- subtract
+ add
* multiply
/ divide

Operators
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
```python
#Boolean builtin methods in python
greeting = ("Hello World")
print(greeting)
print(greeting.isalpha())  # is the string all alphabets
print(greeting.islower())  # is the string lowercase
print(greeting.startswith("H"))  # does the string start with the letter H
print(greeting.endswith("d"))  # does the string end with the letter d
print(greeting.isdigit())  # is the string all digits
```

```python
greeting = "Hello World"
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