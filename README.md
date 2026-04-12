# 🏥 MediData

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A **production-grade FastAPI service** that extracts structured data from hospital bills using a **hybrid OCR + Gemini multimodal pipeline**.

🚀 Built for **ByteVerse Hackathon 2026**

---

## 🎥 Demo

> Replace this with your actual screenshot or demo video

![Demo Screenshot](https://via.placeholder.com/900x400?text=MediData+Demo)

---

## 🧠 Architecture

```
PDF / Image
    │
    ▼
pdf2image (poppler)
    │
    ▼
Image Enhancement (Pillow)
    │
    ├──▶ OCR (Tesseract)
    │
    ▼
Gemini 2.5 Flash (Multimodal)
    │
    ├── Retry + fallback models
    ├── Batch processing
    │
    ▼
Deduplication logic
    │
    ▼
Structured JSON Output
```

---

## ✨ Features

* 🧾 Multimodal AI extraction (image + OCR)
* 📊 Handles tables, handwriting, stamps, rotated text
* 🌐 Multilingual support (English + Hindi)
* 🚫 Prevents duplicate entries (Summary vs Detail pages)
* 🛡️ Fraud detection signals (mismatched values, formatting)
* ⚡ Batch processing for speed optimization
* 🔁 Retry + fallback model support

---

## 📄 API Response Example

```json
{
  "is_success": true,
  "token_usage": {
    "total_tokens": 1234,
    "input_tokens": 1000,
    "output_tokens": 234
  },
  "data": {
    "pagewise_line_items": [
      {
        "page_no": "1",
        "page_type": "Bill Detail",
        "bill_items": [
          {
            "item_name": "BED CHARGE GENERAL WARD",
            "item_amount": 1500.00,
            "item_rate": 1500.00,
            "item_quantity": 1.0
          }
        ]
      }
    ],
    "total_item_count": 42,
    "grand_total": 73420.25
  },
  "error": null
}
```

---

## ⚙️ Setup

### 1. Install System Dependencies

#### Ubuntu / Debian

```bash
sudo apt-get install poppler-utils tesseract-ocr tesseract-ocr-eng tesseract-ocr-hin
```

#### macOS

```bash
brew install poppler tesseract
```

---

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env`:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 4. Run the Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

📘 Swagger UI: http://localhost:8000/docs

---

## 🔌 API Endpoints

| Method | Endpoint             | Description              |
| ------ | -------------------- | ------------------------ |
| GET    | `/health`            | Liveness check           |
| POST   | `/extract-bill-data` | Extract from URL         |
| POST   | `/extract-from-file` | Extract from file upload |

---

### 📤 Extract from URL

```bash
curl -X POST http://localhost:8000/extract-bill-data \
  -H "Content-Type: application/json" \
  -d '{"document": "https://example.com/bill.pdf"}'
```

---

### 📁 Extract from File

```bash
curl -X POST http://localhost:8000/extract-from-file \
  -F "file=@/path/to/bill.pdf"
```

---

## 🧪 Testing

```bash
# Fast (mock mode)
pytest -q

# With real API
USE_MOCK_MODE=false pytest -q -m integration
```

---

## 🐳 Docker

```bash
docker build -t medidata .
docker run -p 8000:8000 --env-file .env medidata
```

---

## 🔑 Environment Variables

| Variable               | Default                            | Description           |
| ---------------------- | ---------------------------------- | --------------------- |
| GOOGLE_API_KEY         | —                                  | Required API key      |
| GEMINI_MODEL           | gemini-2.5-flash                   | Primary model         |
| GEMINI_MODEL_FALLBACKS | gemini-2.0-flash, gemini-1.5-flash | Backup models         |
| MAX_RETRIES            | 5                                  | Retry attempts        |
| BATCH_SIZE             | 3                                  | Pages per API call    |
| PDF_DPI                | 200                                | Rendering DPI         |
| USE_MOCK_MODE          | false                              | Enable mock responses |

---

## 🚀 Why This Project Stands Out

* 🧠 True multimodal AI (not just OCR)
* 📊 Extracts structured data from complex documents
* 🔍 Detects fraud patterns in medical bills
* 🌍 Handles bilingual documents
* ⚡ Optimized for performance and cost
* 🔄 Built with retry and fallback resilience

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py
│   ├── extractor.py
│   └── schemas.py
├── tests/
├── Dockerfile
├── render.yaml
├── requirements.txt
├── pytest.ini
└── .env.example
```

---

## 👨‍💻 Author

Built for **ByteVerse Hackathon 2026**

---

## ⭐ Support

If you found this useful:

👉 Star ⭐ the repo
👉 Share it
👉 Contribute

---

## 📌 Future Improvements

* 📊 Web dashboard (Django/React)
* 📱 Mobile-friendly uploads
* 📈 Analytics & fraud scoring
* 🔐 Secure document storage
