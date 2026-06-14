from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask!"

@app.route('/products')
def products():
    return "Welcome to the products page!"

if __name__ == '__main__':
    app.run(debug=True)