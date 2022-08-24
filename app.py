from email.policy import default
from unicodedata import name
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://student:password@localhost:5432/todoapp'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Todos(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"[{self.id}, {self.description}, {self.completed}]"
    


@app.route('/', methods=["GET", 'POST'])
def index():
    result = Todos.query.all()
    if result != []:
        return render_template('index.html', result=result)
    return render_template('index.html')

@app.route("/todo", methods=["POST"])
def todo():
    if request.method == "POST":
        todo = request.form.get("todo")
        name = request.form.get("id")
        if name != "" and name != None:
            check(name)
        if todo != None and todo != "":
            print("Here")
            new = Todos(description = todo)
            commit_to_db(new)
    return redirect("/")

def check(name):
    try:
        name = name
    except:
        return None
    query = Todos.query.filter(Todos.id==name).first()
    if query.completed == True:
        query.completed = False
    else:
        query.completed = True
    commit_to_db(query)
    return None

def commit_to_db(query):
    try:
        db.session.add(query)
        db.session.commit()
    except:
        db.session.rollback()
    return None
