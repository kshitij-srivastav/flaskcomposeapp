from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from app import Todo
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db. Column(db.String(200), nullable=False)
    desc = db. Column(db. String(500), nullable=False)
    date_created = db. Column(db. DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def hello():
   # todo = todo.show_all()
    return 'Welcome to Home Buddy!!!'


@app.route('/delete/<int:sno>')
def delete(sno):

    # todo = Todo.query.filter_by(sno=sno).first()
    # db.session.delete(todo)
    # db.session.commit()
    # return render_template("index.html")
    return ("Deleting in the second service")


@app.route('/update')
def update():
    todo = todo.show_all()
    return 'Welcome to Update Buddy in diffrent service now arrived from the first!!!'


@app.route('/temp1')
def temp():
    # todo = todo.show_all()
    return 'Deleting the record!!!'


if __name__ == '__main__':
    app.run(port=5006, debug=True)
