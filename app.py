from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///TODO.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    todo=Todo(title="First Task", desc="This is the first task")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')

@app.route('/show')
def products():
    todos=Todo.query.all()
    print(todos)
    return "Todos on the terminal!"

if __name__ == '__main__':
    app.run(debug=True)