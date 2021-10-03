from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import os

from model import process_image

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    imagefile = request.files.get('image')
    full_name = os.path.join(os.getcwd(), 'files', imagefile.filename)
    imagefile.save(full_name)
    return str(process_image(full_name))
    
