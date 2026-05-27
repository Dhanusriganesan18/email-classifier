# Spam/Ham Classification Model

## Overview
This project implements a machine learning pipeline to classify text messages as **spam** or **ham** (legitimate) using multiple classification algorithms. The pipeline includes text preprocessing, feature extraction using TF-IDF vectorization, and model training with various classifiers.

## Project Structure
```
email classifier/
├── data/                          # Dataset folder
├── models/                        # Trained models and visualizations
├── src/
│   └── spam_classifier.py        # Main classifier implementation
├── setup.py                       # Setup script
├── predict_example.py            # Example prediction script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Features

### Text Preprocessing
- URL and email removal
- Special character and digit removal
- Lowercase conversion
- Tokenization
- Stop word removal
- Porter Stemming

### Classification Algorithms
The project implements and compares four algorithms:
1. **Naive Bayes** - Fast and effective for text classification
2. **Logistic Regression** - Linear classifier with good interpretability
3. **Random Forest** - Ensemble method for robust predictions
4. **SVM** - Support Vector Machine for complex boundaries

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
```bash
cd email\ classifier
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download the dataset** (Optional)
   - Download from Kaggle: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
   - Extract `spam.csv` to the `data/` folder
   - If not provided, a sample dataset will be created automatically

## Usage

### Training the Model

Run the main training script:
```bash
python src/spam_classifier.py
```

The script will:
- Load and preprocess the dataset
- Split data into training (80%) and testing (20%) sets
- Train multiple classification models
- Evaluate and compare model performance
- Save the best model and visualizations
- Display detailed metrics and comparisons

### Making Predictions

Use the example prediction script:
```bash
python predict_example.py
```

Or in Python code:
```python
from src.spam_classifier import SpamClassifier

# Load trained model
classifier = SpamClassifier.load_model('models/spam_classifier_model.pkl')

# Make predictions
messages = ["Hello, how are you?", "BUY NOW!!! CLICK HERE!!!"]
predictions = classifier.predict(messages)
probabilities = classifier.predict_proba(messages)

for msg, pred, proba in zip(messages, predictions, probabilities):
    label = "SPAM" if pred == 1 else "HAM"
    print(f"{msg} -> {label} (Confidence: {max(proba)*100:.2f}%)")
```

## Dataset Information

### SMS Spam Collection Dataset
- **Source**: Kaggle (UCI ML Repository)
- **Size**: ~5,574 messages
- **Class Distribution**: ~86.6% ham, ~13.4% spam
- **Features**: Message text

### Columns
- **v1**: Label (ham/spam)
- **v2**: Message text

## Model Performance

Expected performance metrics (with full dataset):
- **Accuracy**: 95-98%
- **Precision**: 90-95%
- **Recall**: 85-95%
- **F1-Score**: 90-95%

## Output Files

After running the training script:
- `models/spam_classifier_model.pkl` - Trained model and vectorizer
- `models/evaluation_plots.png` - Visualization plots including:
  - Confusion Matrix
  - Metrics Comparison
  - Class Distribution
  - ROC Curve

## Key Components

### TextPreprocessor Class
Handles all text preprocessing:
- `clean_text()` - Removes URLs, emails, special characters
- `tokenize_and_stem()` - Tokenizes and applies stemming
- `preprocess()` - Complete preprocessing pipeline

### SpamClassifier Class
Main classification model:
- `train()` - Train the classifier
- `predict()` - Make predictions
- `predict_proba()` - Get probability estimates
- `evaluate()` - Calculate evaluation metrics
- `save_model()` - Save trained model
- `load_model()` - Load trained model

## Feature Engineering

### TF-IDF Vectorization
- Max features: 3000
- N-grams: (1, 2) - unigrams and bigrams
- Min document frequency: 2
- Max document frequency: 0.95

### Text Features
The model learns from:
- Individual words (unigrams)
- Word pairs (bigrams)
- TF-IDF weighted importance

## Results & Insights

### What Works
- Naive Bayes performs excellently on text classification
- Bigrams capture important spam patterns (e.g., "free cash", "click now")
- TF-IDF weighting effectively identifies spam indicators
- Stemming reduces vocabulary and improves efficiency

### Common Spam Patterns
- Urgency words: "NOW", "URGENT", "LIMITED TIME"
- Money-related: "FREE", "CASH", "EARN", "$$$"
- Action words: "CLICK", "BUY", "CALL", "ACT"
- Excessive punctuation and capitalization

## Troubleshooting

### Dataset Not Found
If you see "Dataset not found" message:
1. Download from Kaggle
2. Save as `data/spam.csv`
3. Run again - a sample dataset will be used if needed

### Import Errors
If you get import errors:
```bash
pip install --upgrade scikit-learn nltk pandas numpy
```

### NLTK Data Missing
The script automatically downloads required NLTK data on first run.

## Future Improvements

1. **Deep Learning**: Implement LSTM/GRU models with word embeddings
2. **Word Embeddings**: Use Word2Vec, GloVe, or FastText
3. **Class Imbalance**: Apply SMOTE or weighted classifiers
4. **Hyperparameter Tuning**: Use GridSearchCV or RandomizedSearchCV
5. **Feature Selection**: Apply Chi-square or mutual information
6. **Cross-validation**: Implement k-fold cross-validation
7. **Real-time API**: Deploy as REST API using Flask/FastAPI
8. **Mobile Integration**: Create mobile app for on-device classification

## Performance Optimization

- Use smaller models (Naive Bayes) for real-time predictions
- Implement caching for frequently seen messages
- Use batch processing for large datasets
- Consider model quantization for mobile deployment

## Dependencies

See `requirements.txt` for complete list:
- pandas: Data manipulation
- numpy: Numerical computations
- scikit-learn: Machine learning algorithms
- nltk: Natural Language Processing
- matplotlib & seaborn: Data visualization

## License
This project is open source and available for educational use.

## Author
Machine Learning Practitioner

## Contact & Support
For issues or questions, please refer to the documentation or run:
```bash
python src/spam_classifier.py --help
```

## References
- UCI Machine Learning Repository
- scikit-learn documentation: https://scikit-learn.org/
- NLTK Book: https://www.nltk.org/book/
- TF-IDF Guide: https://en.wikipedia.org/wiki/Tf%E2%80%93idf

---
**Last Updated**: May 2026
