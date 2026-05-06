# Constants: MODEL_NAME, DATA_PATH, SAVE_PATH, TEXT_COL, LABEL_COL.
# Override DATA_PATH / TEXT_COL / LABEL_COL via environment variables.

# compute_metrics(eval_pred) — called by Trainer each eval step.
#   Unpack (logits, labels), argmax logits to get predictions.
#   Return accuracy and weighted F1 using the HuggingFace evaluate library.

# main():
#   1. Load CSV, drop rows missing TEXT_COL or LABEL_COL.
#   2. Encode LABEL_COL to integer ids with LabelEncoder.
#   3. Stratified train/val split (80/20, seed 42).
#   4. Tokenize with DistilBertTokenizerFast, build HuggingFace Datasets.
#   5. Load DistilBertForSequenceClassification with the correct num_labels.
#   6. Configure TrainingArguments: 3 epochs, eval + save per epoch,
#      load_best_model_at_end=True, metric_for_best_model="f1".
#   7. Train, save model + tokenizer to SAVE_PATH.
#   8. Write label_map.json to SAVE_PATH: {int_id: label_string}.
