# 🔄 FLIPMYFILE

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

**FLIPMYFILE** is a clean, modern web application built with Flask that allows users to seamlessly convert between common file formats (PDF, TXT, CSV, and DOC) directly in the browser,

## Features

- **Multi-Format Conversion:**
    - **PDF to:** TXT, CSV, DOC
    - **TXT to:** PDF, CSV, DOC
    - **CSV to:** PDF, TXT, DOC
    - **DOC to:** PDF, TXT, CSV
- **In-Memory Processing:** Files are processed in-memory for security and speed (no temporary files stored on the server).
- **Modern UI:** Responsive design utilizing custom **Eurostile** typography.
- **Dynamic File Naming:** Automatically converts titles to `snake_case` for standardized downloads.

## 🛠️ Tech Stack

- **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
- **Forms:** [Flask-WTF](https://flask-wtf.readthedocs.io/)
- **PDF Handling:** [PyPDF2](https://pypdf2.readthedocs.io/) for reading & [fpdf (For Creating)](http://www.fpdf.org/) for creating
- **Utilities:** [textcase](https://pypi.org/project/textcase/) for filename formatting & [BytesIO](https://docs.python.org/3/library/io.html) for security
- **Styling:** Vanilla CSS with custom fonts

## 📸 Screenshots

<p align="center">
    <img src="static/images/demo_program.png" width="45%" alt="Home Page">
    <img src="static/images/demo_program_2.png" width="45%" alt="Conversion Page">
</p>

## 📁 Project Structure

  ├── components/          # Logic for forms and conversion functions
  ├── static/              # CSS, Fonts, and Images
  ├── templates/           # HTML Jinja2 templates
  ├── app.py               # Main application routes
  └── run.py               # Entry point to start the server

## License

This project is licensed under the MIT License - see the LICENSE file for details.