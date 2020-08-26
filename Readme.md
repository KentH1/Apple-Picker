Read Me (in a Text editor)
----Git Setup----
#To set up a git repository system on the Raspberry Pi follow these steps in the terminal
#To Install Git
sudo apt install git 
#To Setup a Git Folder
cd <Folder Path>  #Create the Folder then enter this to enter its directory
git init  #Initialise Git system
git remote add origin https://github.com/<Repository Owner>/<repository name>.git   #Link to Github repository
git pull https://github.com/<Repository Owner>/<repository name>.git  #Retrieve files currently in the repository
#The folder is now a git system linked to the repository
  

#Useful tools
git add --all #Tells git to track all files in the current directory
git commit -am "<message>"  #Commits changes to the local git system with a brief message
git push -u origin master #Pushes commited changes to the repository, establishes a push path
git push  #pushes commited changes to the repository
git status  #Checks status of uncommited changes
git checkout <branch name>  #changes to specified branch
git checkout -b <branch name>   #Creates a new branch


#If help is required
#https://projects.raspberrypi.org/en/projects/getting-started-with-git
