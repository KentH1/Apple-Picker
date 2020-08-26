Read Me (in a Text editor)
----Git Setup----
#To set up an existing folder as a git repository system on the Raspberry Pi follow these steps in the terminal

 sudo apt install git				#Installs Git 
 cd <Folder Path>				#Enter this to enter the folders directory
 git init    					#Initialise the Git system
 git remote add origin <repository link>.git    #Link to Github repository
 git pull <repository link>.git  		#Retrieve files currently in the repository

#The folder is now a git system linked to the repository
#The repository we are using is: https://github.com/KentH1/Apple-Picker.git

#Useful tools
git add --all 			#Tells git to track all files in the current directory
git commit -am "<message>"  	#Commits changes to the local git system with a brief message
git push -u origin master 	#Pushes commited changes to the repository, establishes a push path
git push			#pushes commited changes to the repository
git status  			#Checks status of uncommited changes
git checkout <branch name>  	#Changes to specified branch
git checkout -b <branch name>   #Creates a new branch


#If help is required
#https://projects.raspberrypi.org/en/projects/getting-started-with-git
