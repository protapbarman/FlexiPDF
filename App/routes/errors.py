from flask import Blueprint, render_template, request, flash, redirect

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(413)
def too_large(e):
    flash('File is too large. Maximum size is 128MB.')
    return redirect(request.url)

@errors.app_errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500
