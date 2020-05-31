# Digital History


## How to use GitHub with the command-line

Install git, a tool for managing code. git is required to use GitHub, the online service from which users can download (pull) and upload (push) code. 

> Install git on Mac: open terminal, install the Xcode toolkit `xcode-select --install`, and install git `git`.

> Install git on Linux: open terminal, install git using the package manager with root privilages (for example, `sudo apt-get install git` in Debian).

> Install git on Windows: download and install [git for Windows](https://git-scm.com/downloads). 

After installing git, open terminal (Mac & Linux) or command prompt (Windows) and navigate to your project folder. 

`cd <path/to/folder>`

Clone the repository to your local folder using the remote URL. The remote URL of any GitHub repository can be found by clicking the green "Clone or download" button in the top right corner.

`git clone <remote URL>`

Add the repository's remote URL as "origin." 

`git remote add origin <remote URL>`

In terminal or command prompt, use the pull command to "pull" the repository into the local folder. 

`git pull origin master`

 * Note: "master" here refers to the master branch. When pulling from another branch, sub master with [name of branch](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches).

_Congrats! You have cloned the respository to your local folder!_

To push code to GitHub, add the files of the local folder to the staging area.

`git add --all`

Commit your changes. 

`git commit -m "an opitional commit message."`

Push your changes to the specified branch (in this example, the master branch). 

`git push origin master`









