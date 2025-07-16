from flask import Blueprint, render_template
from App.controllers.pdf_controller import PDFController

pdf = Blueprint('pdf', __name__, url_prefix='/pdf')
pdf_controller = PDFController()

@pdf.route('/merge', methods=['GET'])
def merge_pdf_page():
    return render_template('pdf/merge.html')

@pdf.route('/merge', methods=['POST'])
def merge_pdfs_route():
    return pdf_controller.merge_pdfs()

@pdf.route('/arrange', methods=['GET'])
def arrange_pdf_page():
    return render_template('pdf/arrange.html')

@pdf.route('/arrange', methods=['POST'])
def arrange_pdf_route():
    return pdf_controller.arrange_pdf()

@pdf.route('/split', methods=['GET'])
def split_pdf_page():
    return render_template('pdf/split.html')

@pdf.route('/split', methods=['POST'])
def split_pdf_route():
    return pdf_controller.split_pdf()

@pdf.route('/convert', methods=['GET'])
def convert_to_pdf_page():
    return render_template('pdf/convert.html')

@pdf.route('/convert', methods=['POST'])
def convert_to_pdf_route():
    return pdf_controller.convert_to_pdf()

@pdf.route('/to-word', methods=['GET'])
def pdf_to_word_page():
    return render_template('pdf/to_word.html')

@pdf.route('/to-word', methods=['POST'])
def pdf_to_word_route():
    return pdf_controller.pdf_to_word()
