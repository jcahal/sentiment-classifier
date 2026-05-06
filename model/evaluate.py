# Load label_map.json from saved_model/ to get id_to_label and label_to_id dicts.
# Reproduce the same val split as train.py (test_size=0.2, seed=42, stratified).
# Load model + tokenizer via model_utils.load_model_and_tokenizer.
# Run model_utils.predict on each val row.
# Print a sklearn classification_report comparing true vs predicted labels.
