# automate-the-boring-stuff
A repository featuring a variety of exercises and projects featured in the book "Automate the Boring Stuff with Python" by Al Sweigart, available at https://automatetheboringstuff.com/


If you are new to programming, and want to learn more about GitHub and some basic commands that are used when utilizing a repository of code, here is a quick overview of GitHub and basic commands that are commonly utilized when compiling code to the online repository from your local directories.


GitHub is a VCS (Version Control System).
For useful commands regarding git versioning, read the git-doc.

```
git rebase --help 
git log --oneline --all --graph
git log
git gc    (garbage collection)
```

How to commit and push changes made on local repository to origin, the following steps can be made: 

```
git commit -a -m "Insert message describing updated content"  
```

The above command adds all tracked files to the staging area and commits them in one step. Where as the push command will push code to the remote repository:
```
git push  
```
Alternatively, to add all files with pending adjustments to the staging area followed by commit use:
```
git add -A
git commit -m "Notes listing changes placed here"
git push
```
Or you could use the following command to track and add all files using this command:
```
git add .
```

To create a new branch from the current branch, use the checkout command:
```
git checkout -b newbranchname
```
The above command creates the new branch and switches to it (checks it out).

If we type:
```
git status
```
We see what branch we are in along with a status update regarding any current and/or pending changes that are staged for commit.

If we type:
```
git branch
```
We get a list of all local branches that we have created using checkout.

In order to push changes from a copied (versioned) branch to the main branch, the following commands can be used:
```
git commit -a -m "Notes listing changes are placed here."
git checkout main  
git pull
git merge versionedBranchNameHere
git push
```

The above command order is important, as pull the main branch will ensure the local branch is up to date before pushing merged changes to the repository.

This is all for now - now let's get to work!

Let's go!!!
