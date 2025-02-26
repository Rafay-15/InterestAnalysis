from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "rafay-15/Roberta-InterestDetection" 

# Load the model and tokenizer from Hugging Face
print(f"Downloading model '{model_name}' from Hugging Face...")
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

save_directory = "model_final"  
print(f"Saving model to '{save_directory}'...")

# Save the model and tokenizer locally
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)

print(f"Model and tokenizer saved successfully to '{save_directory}'!")
