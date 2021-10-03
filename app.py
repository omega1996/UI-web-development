from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
   name = request.args.get('username')
   return  render_template('index.html', name=name)