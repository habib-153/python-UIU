from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def hello_world():
    return "Welcome to Flask world"
# app.add_url_rule('/',  'hello', hello_world)

@app.route('/welcome/<name>')
def hello(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run()
