# to-do-list-app
The application for creating a "to-do list". User can add new tasks and edit, update (to do/done) or delete already existing tasks.

## Technologies
* Python 3.8.5
* Flask 1.1.2
* Flask SQLAlchemy 2.4.4
* psycopg2-binary 2.8.6

## LocalSetup
1) Install All Dependencies  
`pip3 install -r requirements.txt`
2) Database cofiguration  
To make you work easier, find **local_setings.py.example** file, complete it 
with your PostgreSQL data and rename file to **local_setings.py**.  
**Remember!** Do not keep sensitive data under Git's control! (**local_settings.py** file is added to **.gitignore**).   
3) Run the File  
`python3 app.py`
