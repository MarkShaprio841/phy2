from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from PyPDF2 import PdfReader

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    articles = []
    for file in files:
        preview = ""
        try:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], file), 'rb') as f:
                reader = PdfReader(f)
                if len(reader.pages) > 0:
                    text = reader.pages[0].extract_text()
                    preview = ' '.join(text.split()[:30]) + '...'
        except Exception as e:
            preview = "Could not generate preview."
        articles.append({'filename': file, 'preview': preview})
    return render_template('index.html', articles=articles)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
