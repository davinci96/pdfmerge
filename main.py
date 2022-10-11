from crypt import methods
from urllib import request
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import files.merger as mg
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './files'

# files = [pdfs for pdfs in os.listdir('./files') if pdfs.endswith(".pdf")]
# mg.merger(files)

@app.route('/')
def upload_page():
    return render_template('index.html')

@app.route('/upload', methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        files = request.files.getlist("file")
        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        pdf_files = [app.config['UPLOAD_FOLDER'] + '/' + pdfs for pdfs in os.listdir(app.config['UPLOAD_FOLDER']) if pdfs.endswith(".pdf")]
        user_filename = str(request.form.get('file-name'))
        mg.merger(pdf_files, user_filename)

        path = './files/' + user_filename + '.pdf'

        return send_file(path, as_attachment=True)