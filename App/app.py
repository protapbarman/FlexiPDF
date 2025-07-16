from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
from pathlib import Path
from pypdf import PdfReader, PdfWriter
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('pdfs')
        if not files or files[0].filename == '':
            flash('No files selected!')
            return redirect(url_for('index'))
        filenames = []
        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)
        return redirect(url_for('combine', files=','.join(filenames)))
    pdfs = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', pdfs=pdfs)

@app.route('/combine')
def combine():
    files = request.args.get('files', '').split(',')
    writer = PdfWriter()
    for filename in files:
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'combined.pdf')
    with open(output_path, 'wb') as f:
        writer.write(f)
    return send_file(output_path, as_attachment=True)

@app.route('/delete/<filename>')
def delete_file(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(path):
        os.remove(path)
        flash(f'{filename} deleted.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
