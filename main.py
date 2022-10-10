from crypt import methods
from urllib import request
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import files.merger as mg
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/files'

# files = [pdfs for pdfs in os.listdir('./files') if pdfs.endswith(".pdf")]
# mg.merger(files)

@app.route('/')
def upload_page():
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
