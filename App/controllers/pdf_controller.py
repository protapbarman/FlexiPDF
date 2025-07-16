from flask import request, jsonify, send_file, current_app
from werkzeug.utils import secure_filename
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os
import tempfile

class PDFController:
    def __init__(self):
        self.UPLOAD_FOLDER = 'App/uploads'
        self.ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt', 'jpg', 'jpeg', 'png'}

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def merge_pdfs(self):
        if 'files[]' not in request.files:
            return jsonify({'error': 'No files provided'}), 400

        files = request.files.getlist('files[]')
        merger = PdfMerger()

        try:
            for file in files:
                if file and self.allowed_file(file.filename):
                    merger.append(file)

            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                merger.write(temp_file)
                temp_file_path = temp_file.name

            return send_file(
                temp_file_path,
                as_attachment=True,
                download_name='merged.pdf',
                mimetype='application/pdf'
            )
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            merger.close()

    def arrange_pdf(self):
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        page_order = request.form.get('page_order')

        if not file or not self.allowed_file(file.filename):
            return jsonify({'error': 'Invalid file'}), 400

        try:
            return jsonify({'error': 'Feature not implemented yet'}), 501
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def split_pdf(self):
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        split_type = request.form.get('split_type')
        split_value = request.form.get('split_value')

        if not file or not self.allowed_file(file.filename):
            return jsonify({'error': 'Invalid file'}), 400

        try:
            return jsonify({'error': 'Feature not implemented yet'}), 501
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def convert_to_pdf(self):
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if not file or not self.allowed_file(file.filename):
            return jsonify({'error': 'Invalid file'}), 400

        try:
            # TODO: Implement conversion logic based on file type
            # This will require additional libraries based on input file types
            return jsonify({'error': 'Feature not implemented yet'}), 501

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def pdf_to_word(self):
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if not file or not self.allowed_file(file.filename):
            return jsonify({'error': 'Invalid file'}), 400

        try:
            # TODO: Implement PDF to Word conversion
            # Will require additional libraries like pdf2docx
            return jsonify({'error': 'Feature not implemented yet'}), 501

        except Exception as e:
            return jsonify({'error': str(e)}), 500
