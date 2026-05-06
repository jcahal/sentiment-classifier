# Create a FastAPI app with a lifespan handler that loads the model once at startup.
# Add CORS middleware to allow requests from the Vite dev server (localhost:5173).

# GET /health — return a simple status ok response.

# POST /predict — accept a PredictRequest body, run model_utils.predict, return a PredictResponse.
#   Import model_utils from the sibling model/ directory (add it to sys.path).
#   Use module-level variables for model, tokenizer, and label_map so the endpoint can reach them.
