import os 
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

# Gets the base path
basedir = os.path.abspath(os.path.dirname(__file__))

# Creates placeholder information 
UPLOAD_FOLDER = basedir + '/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# function for determining if a file name is valid 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Creates an app 
app = Flask(__name__)

# CONFIGURATION OF APP
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


    file_names = os.listdir('static/uploads')
    return render_template('homepage.html', file_names=file_names)


@app.route('/document/<filename>')
def doc(filename):
    return f"hello {filename}" 


if __name__ == '__main__':
    app.run(debug=True)