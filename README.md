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

# Go to Dagshub url and create a new account and link your github repo to it 
# go to the selected repo and select remote option from there and go to the Experiment tab ans u can find the dagshub url 
    -->import dagshub
        dagshub.init(repo_owner='bhaskarmaddala', repo_name='MLProjectEndtoEnd', mlflow=True)

        import mlflow
        with mlflow.start_run():
        mlflow.log_param('parameter name', 'value')
        mlflow.log_metric('metric name', 1)

    --> https://dagshub.com/bhaskarmaddala/MLProjectEndtoEnd.mlflow