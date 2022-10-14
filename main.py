from crypt import methods
from urllib import request
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import files.merger as mg
import os
import sys

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './files/temp'

@app.route('/')
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods = ['GET','POST'])
def upload():
    try:
        if request.method == 'POST':
            files = request.files.getlist("file")
            
            for file in files:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            pdf_files = [app.config['UPLOAD_FOLDER'] + '/' + pdfs for pdfs in os.listdir(app.config['UPLOAD_FOLDER']) if pdfs.endswith(".pdf")]
            user_filename = str(request.form.get('file-name')) + '.pdf'
            mg.merger(user_filename, pdf_files)

            path = './files/result/' + user_filename

            return send_file(path, as_attachment=True)
    except Exception as err:
        return render_template('error.html', err=err.__class__)