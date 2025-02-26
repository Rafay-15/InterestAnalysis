```markdown
# Interest Analysis Model 🎯  

This repository contains a fine-tuned transformer model for **intent analysis**, built on `j-hartmann/emotion-english-distilroberta-base`.  
The model classifies text into three categories:  
✅ **Disinterested**  
✅ **Neutral**  
✅ **Interested**  

This model is useful for analyzing customer feedback, social media interactions, and other text-based user intent scenarios.

## 📂 Repository Structure
```
.
├── download_model.py   # Downloads the model from Hugging Face
├── run_model.py        # Loads the model and runs predictions
├── requirements.txt    # Required dependencies
├── README.md           # Project documentation
└── downloaded_model/   # (Automatically created) Directory where the model is saved
```

## 🚀 Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Rafay-15/InterestAnalysisModel.git
cd InterestAnalysisModel
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

## 📥 Download the Model  
To download the fine-tuned model from Hugging Face:  
```bash
python hf.py
```
This will create a `model_final/` directory containing the model and tokenizer.

## 🔄 Run the Model with Example Texts  
Once the model is downloaded, you can test it with sample inputs:  
```bash
python main.py
```

### **Expected Output**
```
--- Model Predictions ---
Text: I absolutely love this! -> Predicted Label: interested
Text: I don't care about this at all. -> Predicted Label: disinterested
Text: It's fine, I guess. -> Predicted Label: neutral
```


## 📜 License  
This project is released under the **MIT License**. Feel free to use and modify it for research and commercial purposes.

## 🤝 Contributing  
If you'd like to contribute or improve the model, feel free to fork the repo and submit a pull request.

## 🔗 Links  
- 🤗 **Hugging Face Model**: [https://huggingface.co/rafay-15/Roberta-InterestDetection](https://huggingface.co/rafay-15/Roberta-InterestDetection)  
- 📂 **GitHub Repository**: [https://github.com/Rafay-15/InterestAnalysisModel](https://github.com/Rafay-15/InterestAnalysis)  

🚀 **Happy coding!** 🎯
