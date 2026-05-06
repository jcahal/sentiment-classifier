# load_model_and_tokenizer(model_path) — load a saved DistilBERT tokenizer and model from disk.
#   Set model to eval mode. Return both.

# predict(text, model, tokenizer, label_map, max_length=512) — run inference on a single string.
#   label_map is {int_id: label_string}.
#   Return {"label": "...", "confidence": 0.94}.
