# 🧠 Sentiment Classifier — PyTorch + HuggingFace + FastAPI + Vue.js

> Real-time text sentiment analysis powered by a fine-tuned DistilBERT model, served via FastAPI, and wrapped in a clean Vue.js interface.

🔗 **Live Demo:** _coming soon_
📸 **Demo GIF:** _coming soon_

---

## 📌 Overview

This project fine-tunes `distilbert-base-uncased` on a labeled sentiment dataset and exposes predictions through a REST API. A Vue.js frontend lets users type any text and receive an instant positive/negative sentiment prediction with a confidence score.

This is a full-stack ML application — model training, API serving, and a working UI — deployed and accessible without running a single notebook.

---

## 🗂 Project Structure

```
sentiment-classifier/
├── model/
│   ├── train.py              # Fine-tuning script (HuggingFace Trainer API)
│   ├── evaluate.py           # Eval metrics on test split
│   ├── model_utils.py        # Tokenizer + model loading helpers
│   └── saved_model/          # Serialized weights (gitignored)
│
├── api/
│   ├── main.py               # FastAPI app + /predict endpoint
│   ├── schemas.py            # Pydantic request/response models
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.vue
│   │   ├── components/
│   │   │   └── SentimentForm.vue
│   │   └── main.js
│   ├── public/
│   └── package.json
│
├── .gitignore
├── docker-compose.yml        # Optional: local full-stack dev
└── README.md
```

---

## 🛠 Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Model     | PyTorch + HuggingFace Transformers  |
| API       | FastAPI + Uvicorn                   |
| Frontend  | Vue.js 3 (Composition API)          |
| Deployment| Railway / Render / AWS App Runner   |

---

## 🚀 Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/sentiment-classifier.git
cd sentiment-classifier
```

### 2. Train the model
```bash
cd model
pip install -r requirements.txt
python train.py
```

### 3. Run the API
```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

API will be live at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

### 4. Run the frontend
```bash
cd frontend
npm install
npm run dev
```

Frontend will be live at `http://localhost:5173`

---

## 📡 API Reference

### `POST /predict`

**Request**
```json
{
  "text": "This movie was absolutely fantastic!"
}
```

**Response**
```json
{
  "label": "POSITIVE",
  "confidence": 0.9871
}
```

---

## 📊 Model Details

| Property        | Value                          |
|-----------------|--------------------------------|
| Base Model      | `distilbert-base-uncased`      |
| Dataset         | _[your dataset here]_          |
| Training Epochs | 3                              |
| Optimizer       | AdamW                          |
| Accuracy        | _[fill in after training]_     |
| F1 Score        | _[fill in after training]_     |

---

## 🗺 Roadmap

- [x] Project scaffold and README
- [ ] Data preprocessing pipeline
- [ ] Fine-tune DistilBERT on sentiment dataset
- [ ] FastAPI `/predict` endpoint
- [ ] Vue.js frontend with live prediction
- [ ] Deploy API to Railway/Render
- [ ] Add live demo URL + demo GIF to README

---

## 🤝 Contributing

This is a portfolio project. Issues and suggestions are welcome.

---

## 📄 License

MIT