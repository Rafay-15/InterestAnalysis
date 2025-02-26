import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Define the local model path (after downloading)
model_path = "model_final" 

# Load the model and tokenizer
print(f"Loading model from '{model_path}'...")
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Define label mapping
id2label = {0: "disinterested", 1: "neutral", 2: "interested"}

def predict(text):
    """Predicts the intent category of the input text."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    
    return id2label[predicted_class]

# Example texts for testing
test_sentences = [
    "I absolutely love this!",
    "I don't care about this at all.",
    "It's fine, I guess."
]

print("\n--- Model Predictions ---")
for sentence in test_sentences:
    print(f"Text: {sentence} -> Predicted Label: {predict(sentence)}")
