from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
   name = request.args.get('username')
   return  render_template('index.html', name=name)