# to-do-list-app
A simple application for creating your own "to-do lists". It gives you possibility to add, edit, update (to do/done) and delete tasks.

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
