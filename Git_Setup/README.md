
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

### Git commands

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
