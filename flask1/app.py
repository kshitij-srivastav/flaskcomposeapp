
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db. Column(db.String(200), nullable=False)
    desc = db. Column(db. String(500), nullable=False)
    date_created = db. Column(db. DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    alltodo = Todo.query.all()

    return render_template("index.html", alltodo=alltodo)


@app.route('/delete/<int:sno>')
def delete(sno):
    url = "http://192.168.52.125:5006/delete/"+str(sno)
    return redirect(url)
    # return "Deleting from it wait"


@app.route('/update')
def update():
    url = "http://192.168.52.125:5006/update/"
    return redirect(url)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
