# PDF Combiner Flask App

A modern Flask web application to upload, view, delete, and combine PDF files using a browser interface. The UI uses Tailwind CSS for a clean look.

## Features
- Drag-and-drop or select PDF files for upload
- List uploaded PDFs
- Delete unwanted PDFs
- Combine selected PDFs into one file
- Download the combined PDF

## Setup
1. Create and activate a Python virtual environment.
2. Install dependencies:
   ```bash
   pip install flask pypdf werkzeug
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser at http://127.0.0.1:5000

## Folder Structure
- `app.py`: Main Flask application
- `templates/`: HTML templates
- `static/`: Static files (for future use)
- `uploads/`: Uploaded PDF files

## Notes
- Tailwind CSS is loaded via CDN for simplicity.
- Uploaded files are stored in the `uploads` folder.
