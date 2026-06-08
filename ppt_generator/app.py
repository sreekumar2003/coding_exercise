"""
Flask application entry point for the Modern PPT Generator.
"""

import os
from pathlib import Path

from flask import (
    Flask,
    render_template,
    request,
    send_file,
    jsonify,
)
from werkzeug.utils import secure_filename
import io

from utils.extractor import extract_text
from utils.structurer import structure_content
from utils.ppt_creator import create_pptx

# ── App setup ─────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
UPLOAD_FOLDER = BASE_DIR / "uploads"
UPLOAD_FOLDER.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {".pptx", ".ppt", ".pdf", ".txt", ".md"}
MAX_CONTENT_MB = 20

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_MB * 1024 * 1024
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")


def _allowed(filename: str) -> bool:
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/")
def index():
    return render_template("index.html")


@app.post("/generate")
def generate():
    """
    Accepts either:
      - multipart/form-data with a 'file' field (PPT / PDF / TXT)
      - form field 'plain_text' with raw text
    Also reads 'theme' form field ("dark" | "light" | "minimal").
    Returns the generated .pptx file as a download.
    """
    theme = request.form.get("theme", "dark")
    plain_text = request.form.get("plain_text", "").strip()
    uploaded_file = request.files.get("file")

    file_bytes = None
    filename = None

    if uploaded_file and uploaded_file.filename:
        if not _allowed(uploaded_file.filename):
            return jsonify(error="Unsupported file type. Please upload .pptx, .pdf, or .txt"), 400
        filename = secure_filename(uploaded_file.filename)
        file_bytes = uploaded_file.read()

    try:
        raw_text = extract_text(file_bytes, filename, plain_text)
    except ValueError as exc:
        # exc is always raised by our own code with a safe user-facing message
        return jsonify(error=exc.args[0] if exc.args else "Invalid input."), 400

    slides = structure_content(raw_text)
    pptx_bytes = create_pptx(slides, theme_name=theme)

    stem = Path(filename).stem if filename else "presentation"
    output_name = f"{stem}_modern.pptx"

    return send_file(
        io.BytesIO(pptx_bytes),
        mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        as_attachment=True,
        download_name=output_name,
    )


@app.post("/preview")
def preview():
    """Return slide structure as JSON (for front-end preview)."""
    theme = request.form.get("theme", "dark")
    plain_text = request.form.get("plain_text", "").strip()
    uploaded_file = request.files.get("file")

    file_bytes = None
    filename = None

    if uploaded_file and uploaded_file.filename:
        if not _allowed(uploaded_file.filename):
            return jsonify(error="Unsupported file type."), 400
        filename = secure_filename(uploaded_file.filename)
        file_bytes = uploaded_file.read()

    try:
        raw_text = extract_text(file_bytes, filename, plain_text)
    except ValueError as exc:
        return jsonify(error=exc.args[0] if exc.args else "Invalid input."), 400

    slides = structure_content(raw_text)
    return jsonify(slides=slides, theme=theme, total=len(slides))


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug, port=5000)
