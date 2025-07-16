# FlexiPDF
A straight forward pdf manage app

## Features
- merge pdfs
- split pdf
- organize pdf
- convert to pdf
- pdf to word
- Resume Parser/Rating

## Setup
1. Create and activate a Python virtual environment.
   ```bash
   python -m venv venv
   venv/Scripts/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   flask run
   ```
4. Open your browser at http://127.0.0.1:5000


## Future Plans

- Features
   - split pdf (Should have pdf viewer container with arrow button pagination and page number mentioning below)
   - organize pdf (Should load all pages separately as cards(with old and new page number mentioning below) to drag and reorganize order)
   - convert to pdf (doc, docx, xls, xlsx, pptx, md, jpg, jpeg, png)
   - pdf to word (docx)
   - Resume Parser/Rating (no OCR)

- Data Manage
   - Authentication is not requried
   - Give user option to allow us to store their processed files/data (simple yes/no and that's it)
   - MongoDB expected collections will be:
      - files
      - resume_data