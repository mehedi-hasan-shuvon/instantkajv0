//to see which directory we are in
pwd

//setting name and mail
git config --global user.name "mehedi"
git config --global user.email "mehedi.hasan.shuvon@gmail.com"
git --list

//to show name nad email
git config user.name 
git config user.name 

// to chcek a git status
git status

//to make a git repository
git init

// to send all file into statging phrase
git add --a

//to commit
git commit -m "initial status"

// to  make a file untracked forever
git rm --cached filename.txt


//to send perticular file to stating pharse
git add filename.txt

//then to commit
git commit -m "string"

// to delete all the file in the repository
rm -rf .git

//to clone a github repository
git clone  {url} foldername


// to make a file ignore first make a file name .gitignore
touch .gitignore
//then add the file name what should be ignored inside the .gitignore 

//to compare between working area and staging area
git diff
git diff --staged

// to do direct commit without staging
git commit -a -m "direct commit"

// to see all the past commit 
git log
q <..... to exit

// to see what change has been in past commit brifly
git log -p
q <..... to exit

//to see change in a statistic way(summary)
git log --stat

//to see what is the change in the commit history
git log --pretty=full

//to see what commit has done in 2 days
git log --since=2.days

// to delete any thing in the repository
git rm filename.txt

//to change past commited file in that past commit 
git commit --amend

// to make a staged file unstaged 
git restore --staged readme.txt

// to restore last modification
(it only work on modified file staged file will not change)
git checkout -- filename.txt

// to go to previous commit from modified statged
git checkout -f

//to make a short cut  command of a long command
git config --global alias.st status (for example here git st will mean git status)
git config --global alias.unstage 'restore --staged--' (to unsatge a file)
git config --global alias.last 'log -p -1'  (to see last commit)



...............<GitHub>..............................
(pull: code send github to our local system)
(push:code send local system to github)

// remote is the hosting on github(to add with github
first time we have to write it)
//to check if we have a repository connected with github
git remote

//to connect with github 
git remote add origin {github urls}

//to see which url is used for push and poll
git remote -v

// to push something on git
git branch -M main (only for the first time)
git push -u origin  main

<<<<<<< HEAD
...............<branching>..........
//to create new branch
git  checkout -b branchname

//to switch between branches
git checkout branchname

//to see all the branch  list
git branch
//to see all the last commit of all branch
git branch -v

git branch --merged(to see which branch already marged)
git branch --no-merged(to see not merged branch)

//to  delete brnach
git branch -d brnachname (give error if not merged)
=======

//to create ssh key
git remote add origin git@github.com:mehedi-hasan-shuvon/push2.git
ssh-keygen -t rsa -b 4096 -C "mehedi.hasan.shuvon@gmail.com"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
tail ~/.ssh/id_rsa.pub



............<branching>...................
// to create a branch and swich into it 
git checkout -b develop

// to change branch 
git checkout branchname
//to check git all the branch
git branch
 
//to merge brach with master
git merge branchname

// to send beanch to github
git push origin branchname
........................<git branch  marge conflict>.......................

this is added at bugfix branch