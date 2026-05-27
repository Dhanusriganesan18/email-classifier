## QUICK START GUIDE

### Option 1: Train the Model (With Sample Data - FASTEST)
```bash
# Navigate to project directory
cd "c:\Users\GANESAN\Documents\email classifier"

# Run training (uses sample dataset automatically)
python src/spam_classifier.py
```
Output: Trained model + evaluation metrics + visualization plots

---

### Option 2: Train with Full Kaggle Dataset (BETTER RESULTS)

#### Step 1: Download Dataset
1. Go to: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
2. Click "Download" (requires Kaggle account)
3. Extract the downloaded file
4. Find `spam.csv`

#### Step 2: Place Dataset
```bash
# Copy spam.csv to the data folder
copy path\to\spam.csv "c:\Users\GANESAN\Documents\email classifier\data\spam.csv"
```

#### Step 3: Run Training
```bash
cd "c:\Users\GANESAN\Documents\email classifier"
python src/spam_classifier.py
```

---

### Option 3: Use Pre-trained Model for Predictions
```bash
# Make predictions with trained model
python predict_example.py
```

---

### Project File Locations

| File | Purpose |
|------|---------|
| `src/spam_classifier.py` | Main training script |
| `predict_example.py` | Example predictions |
| `generate_documentation.py` | Generate Word document |
| `models/spam_classifier_model.pkl` | Trained model (created after training) |
| `models/evaluation_plots.png` | Visualization plots |
| `SPAM_CLASSIFICATION_PROJECT_REPORT.docx` | Project documentation |

---

### Expected Output

After running `python src/spam_classifier.py`, you'll see:
```
============================================================
SPAM/HAM CLASSIFICATION MODEL
============================================================

Creating sample dataset for demonstration...
✓ Sample dataset created: 20 messages

Training naive_bayes model...
✓ Model trained successfully!

Evaluating naive_bayes model...
============================================================
Classification Report - NAIVE_BAYES
============================================================
Accuracy:  0.7500
Precision: 1.0000
Recall:    0.5000
...
```

---

### Using the Model in Your Own Code

```python
from src.spam_classifier import SpamClassifier

# Load trained model
classifier = SpamClassifier.load_model('models/spam_classifier_model.pkl')

# Single prediction
result = classifier.predict(["Hello, how are you?"])
print(result)  # 0 = Ham, 1 = Spam

# Get probabilities
proba = classifier.predict_proba(["Hello, how are you?"])
print(proba)  # [ham_prob, spam_prob]

# Batch predictions
messages = [
    "Hey, meeting at 3pm?",
    "BUY NOW!!! CLICK HERE!!!",
    "Thanks for your help"
]
predictions = classifier.predict(messages)
```

---

### Troubleshooting

**Dataset not found?**
→ Run with sample data first: `python src/spam_classifier.py`

**Import errors?**
→ Install dependencies: `pip install -r requirements.txt`

**NLTK data missing?**
→ Script downloads automatically on first run

**Model file missing?**
→ Run training first: `python src/spam_classifier.py`

