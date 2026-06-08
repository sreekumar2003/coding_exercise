# Modern PPT Generator

A Flask web application that converts **PPT / PDF / plain text** into a polished, modern PowerPoint presentation.

## Features

| Input | Details |
|---|---|
| `.pptx` / `.ppt` | Extracts text from every slide |
| `.pdf` | Extracts text from every page |
| `.txt` / `.md` | Accepts raw text |
| Plain text (paste) | Accepts text pasted directly in the browser |

**Three built-in themes:** Dark · Light · Minimal

**Smart slide structuring:**  
Headings are auto-detected and become slide titles; body lines become bullet points. Explicit slide/page markers from the extractor are honoured.

**Live preview:** See the slide structure before downloading.

---

## Quick Start

```bash
cd ppt_generator
pip install -r requirements.txt
python app.py
```

Open <http://localhost:5000> in your browser.

---

## Project Structure

```
ppt_generator/
├── app.py                  # Flask application (routes)
├── requirements.txt
├── utils/
│   ├── extractor.py        # Text extraction from PPTX / PDF / TXT
│   ├── structurer.py       # Converts raw text → list of Slide dicts
│   └── ppt_creator.py      # Builds a modern .pptx from Slide dicts
├── templates/
│   └── index.html          # Web UI
└── static/
    ├── css/style.css
    └── js/app.js
```

---

## API Endpoints

### `POST /generate`
Returns a `.pptx` file download.

| Field | Type | Description |
|---|---|---|
| `file` | file | Optional `.pptx`, `.pdf`, `.txt`, or `.md` |
| `plain_text` | string | Optional pasted text |
| `theme` | string | `dark` \| `light` \| `minimal` (default: `dark`) |

### `POST /preview`
Returns JSON with the structured slide list.

```json
{
  "slides": [
    { "title": "AI in Healthcare", "bullets": [], "layout": "title" },
    { "title": "Introduction",     "bullets": ["…", "…"], "layout": "bullets" }
  ],
  "theme": "dark",
  "total": 6
}
```
