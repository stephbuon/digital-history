# placeholdertitle


## How to use GitHub with the command-line

1. Install git, an open-source tool for managing code. Installing git is necessary for using GitHub, the online service from which users can download (pull) and upload (push) code. 

Installing git on Mac:
 - open terminal
 - install the Xcode toolkit. Type: `xcode-select --install`
 - install git. Type: `git`

Installing git on Linux: 
 - open terminal
 - using package manager ------ 

Installing git on Windows:
 - Download and install [git for Windows](https://git-scm.com/downloads) 

2. in terminal navigate to your project folder. 

On Mac and Linux:
`cd <name of your project folder>`


On Windows:

3. add the remote URL as origin.

`git remote add origin < >`


4. use the pull command to "pull" the repository into the local folder. 

`git pull origin master`

Note: "master" here refers to the master branch. When pulling from another branch, sub master with name of branch.

Congrats! You now have cloned the respository onto your desktop! 
To 

1. add the current files in the local folder to the staging area. 
`git add --all`

2. commit your changes. 
`git commit -m "an opitional commit message."`

3. push your changes to the specified branch (in this example, the master branch). 
`git push origin master`









