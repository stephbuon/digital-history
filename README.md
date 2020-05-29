# placeholdertitle


## How to use GitHub with the command-line

Install git, an open-source tool for managing code. Installing git is necessary for using GitHub, the online service from which users can download (pull) and upload (push) code. 

 - on Mac:
   - open terminal
   - install the Xcode toolkit. Type: `xcode-select --install`
   - install git. Type: `git`

 - on Linux: 
   - open terminal
   - install git using your package manager (for example, `apt-get` in Debian or `sudo pacman` in Arch) with root privilages. 
     - for example: `sudo apt-get install git`

 - on Windows:
   - Download and install [git for Windows](https://git-scm.com/downloads) 

In terminal (Mac & Linux) or command prompt (Windows) navigate to your project folder. 

`cd <path/to/folder>`

Add the remote URL as origin. The remote URL of any GitHub repository can be copied by clicking the green "Clone or download" button in the top right corner.

`git remote add origin <remote URL>`

In terminal or command prompt, use the pull command to "pull" the repository into the local folder. 

`git pull origin master`

Note: "master" here refers to the master branch. When pulling from another branch, sub master with [name of branch](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches).

Congrats! You have cloned the respository to your local directory! 

1. add the current files in the local folder to the staging area. 
`git add --all`

2. commit your changes. 
`git commit -m "an opitional commit message."`

3. push your changes to the specified branch (in this example, the master branch). 
`git push origin master`









