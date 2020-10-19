from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

try:
    from local_settings import postgresql_config
except ImportError:
    print("Make a PostgreSQL configuration in 'local_settings.py' and then try again.")
    postgresql_config = None
    exit(1)

# in 'local_settings.py':
# postgresql_config: str = 'postgresql+psycopg2://<user>:<password>@localhost/<database_name>'

app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ToDoList(db.Model):
    __tablename__: str = 'to_do_list'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(240))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    """
    Main page with a list of all tasks
    """
    todo_list = ToDoList.query.all()
    return render_template('main_page.html', todo_list=todo_list)


@app.route('/add', methods=['POST'])
def add():
    """
    Adding a new task
    """
    task = request.form.get('task')
    new_todo = ToDoList(task=task, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    """
    Updating a task (done/to do)
    :param todo_id: an id of a task
    :type todo_id: integer
    """
    todo = ToDoList.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/edit/<int:todo_id>', methods=['POST', 'GET'])
def edit(todo_id):
    """
    Editing a task
    :param todo_id: an id of a task
    :type todo_id: integer
    """
    if request.method == 'GET':
        edit_todo = ToDoList.query.filter_by(id=todo_id).first()
        return render_template('edit_task.html', edit_todo=edit_todo)
    if request.method == 'POST':
        edit_todo = ToDoList.query.filter_by(id=todo_id).first()
        edit_todo.task = request.form.get('edit_task')
        db.session.add(edit_todo)
        db.session.commit()
    return redirect('/')


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    """
    Deleting a task
    :param todo_id: an id of a task
    :type todo_id: integer
    """
    todo = ToDoList.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == '__main__':
    # creating tables in your database
    db.create_all()
    app.run()
