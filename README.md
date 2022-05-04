# automate-the-boring-stuff
A repository featuring a variety of exercises and projects featured in the book "Automate the Boring Stuff with Python" by Al Sweigart, available at https://automatetheboringstuff.com/

GitHub is a VCS (Version Control System)
For useful commands regarding git versioning, read the git-doc
git rebase --help 
git log --oneline --all --graph
git log
git gc    (garbage collection)

How to commit and push changes made on local repository to origin, the following steps can be made.
git commit -a -m "Insert message describing updated content"  (adds all tracked files to the staging area and commits them in one step)
git push  (Pushes commits to remote repository)

Alternatively, to add all files with pending adjustments to the staging area followed by commit use:
git add -A
git commit -m "some message"
git push

to create a new branch from the current branch, use the checkout command:
git checkout -b newbranchname
the above command creates the new branch and switches to it.

typing 'git status' now will show you a message indicating that you are now in the 'newbranchname' branch
typing 'git branch' will show you a list of all branches associated with repository, along with the branch you are in.

in order to push changes from the copied (versioned) branch to the main branch, the following commands can be used:
