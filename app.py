from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

try:
    from local_settings import postgresql_config
except ImportError:
    print("Make a PostgreSQL configuration in 'local_settings.py' and then try again.")
    postgresql_config = None
    exit(0)

# in 'local_settings.py':
# postgresql_config= postgresql+psycopg2://<user>>:<password>@localhost/<database_name>'
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ToDoList(db.Model):
    __tablename__ = 'to_do_list'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(240))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    # show all todos
    todo_list = ToDoList.query.all()
    return render_template('main_page.html', todo_list=todo_list)


@app.route('/add', methods=['POST'])
def add():
    # add new task
    task = request.form.get('task')
    new_todo = ToDoList(task=task, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    # update task
    todo = ToDoList.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # delete task
    todo = ToDoList.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == '__main__':
    # db.create_all()
    app.run()
