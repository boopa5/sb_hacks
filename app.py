import os 
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from pdf2image import convert_from_path

# Gets the base path
basedir = os.path.abspath(os.path.dirname(__file__))

# Creates placeholder information 
UPLOAD_FOLDER = basedir + '/static/uploads'
IMAGE_FOLDER = basedir + '/static/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# function for determining if a file name is valid 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Creates an app 
app = Flask(__name__)

# CONFIGURATION OF APP
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            pages = convert_from_path(file_path, 500)

            if pages:
                first_page_image = pages[0]
                image_filename = secure_filename(f"{filename[:-4]}.jpg")
                image_path = os.path.join(app.config['IMAGE_FOLDER'], image_filename)
                first_page_image.save(image_path, 'JPEG')


            # pages = convert_from_path(file, 500)
            # pages[0].save(IMAGE_FOLDER, filename, 'JPEG')


    file_names = os.listdir('static/uploads')
    return render_template('homepage.html', file_names=file_names)


@app.route('/document/<filename>')
def doc(filename):
    return render_template('document.html', file=filename)


if __name__ == '__main__':
    app.run(debug=True)