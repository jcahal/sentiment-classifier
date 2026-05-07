# Sentiment Classifier — PyTorch + HuggingFace + FastAPI + Vue.js

Real-time text sentiment analysis powered by a fine-tuned DistilBERT model, served via FastAPI, and wrapped in a clean Vue.js interface.

---

## Project Structure

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
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── App.vue
│   │   ├── components/
│   │   │   └── SentimentForm.vue
│   │   └── main.js
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── Dockerfile
│
├── pytorch_bert_example.ipynb
├── Articles.csv
├── Dockerfile                # Notebook / ML dev environment
├── requirements.txt          # ML dependencies
├── docker-compose.yml
└── README.md
```

---

## Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Model     | PyTorch + HuggingFace Transformers  |
| API       | FastAPI + Uvicorn                   |
| Frontend  | Vue.js 3 (Composition API) + Vite   |
| Dev Env   | Docker Compose                      |

---

## Quickstart

### Option A — Docker (recommended)

```bash
# 1. Train the model first (required before starting the api)
docker compose run --rm shell bash -c "cd model && python train.py"

# 2. Start everything
docker compose up
```

| Service  | URL                          |
|----------|------------------------------|
| Frontend | http://localhost:5173        |
| API docs | http://localhost:8000/docs   |
| Notebook | http://localhost:8888        |

```bash
# Open an interactive Python shell
docker compose run --rm shell
```

### Option B — Local

**Train the model**
```bash
pip install -r requirements.txt
cd model && python train.py
```

**Run the API**
```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
# → http://localhost:8000
```

**Run the frontend**
```bash
cd frontend
npm install
npm run dev
# → http://localhost:5173
```

---

## API Reference

### `POST /predict`

**Request**
```json
{ "text": "This article was incredibly insightful!" }
```

**Response**
```json
{ "label": "POSITIVE", "confidence": 0.9871 }
```

### `GET /health`
```json
{ "status": "ok" }
```

---

## Model Details

| Property        | Value                          |
|-----------------|--------------------------------|
| Base Model      | `distilbert-base-uncased`      |
| Dataset         | `Articles.csv` (configurable)  |
| Training Epochs | 3                              |
| Optimizer       | AdamW                          |

**Configuration via environment variables:**

| Variable   | Default          | Description                    |
|------------|------------------|--------------------------------|
| `DATA_PATH`| `../Articles.csv`| Path to training CSV           |
| `TEXT_COL` | `Article text`   | Column containing input text   |
| `LABEL_COL`| `Category`       | Column containing labels       |

---

## Roadmap

- [x] Project scaffold and README
- [x] Docker Compose dev environment (notebook, shell, api, frontend)
- [ ] Model training pipeline (DistilBERT + HuggingFace Trainer)
- [ ] FastAPI `/predict` endpoint
- [ ] Vue.js frontend with live prediction
- [ ] Data preprocessing pipeline
- [ ] Fine-tune on labeled sentiment dataset
- [ ] Deploy API to Railway/Render
- [ ] Add live demo URL + demo GIF to README

---

## License

MIT
