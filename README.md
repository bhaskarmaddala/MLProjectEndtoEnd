# This is my End to end Project

# TODO:Below Step 
# 1) First initlize the git 
    -->git init
# 2)If we want to add the file and commit the 
#   git add <<FileName>>
      eg: git add README.md
#    If you want to add complete directory the 
    -->git add .

# 3)Now need to commit
    -->git commit -m "This is my first Commit"

# 4)to get the updated code from github 
    -->git pull

# 5) Create sh file to run the bash file 
    --> bash init_setup.sh
# sometimes environment will not be created in that case we need to activate the source env script manually
    --> source activate ./env

# in Requirements.txt file if we mention -e . in it then it will internally call setup.py file....

# TO RUN THS LOCAL PACKAGE RUN BELOW COMMAND
    --> python setup.py install 

# another way to install requirements.txt is incluide "-e ." and run below command
    --> pip install -r requirements.txt