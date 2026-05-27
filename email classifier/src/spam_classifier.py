"""
Spam/Ham Classification Model
This script implements a machine learning pipeline to classify messages as spam or ham
using text preprocessing and various classification algorithms.
"""

import os
import pandas as pd
import numpy as np
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import warnings

warnings.filterwarnings('ignore')

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, confusion_matrix, classification_report,
                             roc_auc_score, roc_curve)
import matplotlib.pyplot as plt
try:
    import seaborn as sns
    sns.set_palette("husl")
except ImportError:
    sns = None

# Configure plotting
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    plt.style.use('default')

class TextPreprocessor:
    """Handles text preprocessing for spam classification"""
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
    
    def clean_text(self, text):
        """
        Clean text by removing URLs, special characters, and converting to lowercase
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)
        
        # Remove special characters and digits (keeping only letters and spaces)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def tokenize_and_stem(self, text):
        """
        Tokenize text and apply stemming
        """
        tokens = word_tokenize(text)
        tokens = [self.stemmer.stem(word) for word in tokens 
                  if word not in self.stop_words and len(word) > 2]
        return ' '.join(tokens)
    
    def preprocess(self, text):
        """
        Apply full preprocessing pipeline
        """
        text = self.clean_text(text)
        text = self.tokenize_and_stem(text)
        return text


class SpamClassifier:
    """Main spam classification model"""
    
    def __init__(self, model_type='naive_bayes'):
        """
        Initialize classifier with specified model type
        
        Args:
            model_type: 'naive_bayes', 'logistic_regression', 'random_forest', or 'svm'
        """
        self.preprocessor = TextPreprocessor()
        self.model_type = model_type
        self.vectorizer = TfidfVectorizer(max_features=3000, 
                                          ngram_range=(1, 2),
                                          min_df=2,
                                          max_df=0.95)
        self.model = self._get_model()
        self.metrics = {}
    
    def _get_model(self):
        """Get the classifier model based on model_type"""
        models = {
            'naive_bayes': MultinomialNB(),
            'logistic_regression': LogisticRegression(max_iter=1000, random_state=42),
            'random_forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'svm': SVC(kernel='rbf', probability=True, random_state=42)
        }
        return models.get(self.model_type, MultinomialNB())
    
    def preprocess_texts(self, texts):
        """Preprocess a list of texts"""
        return [self.preprocessor.preprocess(text) for text in texts]
    
    def train(self, X_train, y_train):
        """
        Train the classifier
        
        Args:
            X_train: Training texts
            y_train: Training labels (0 for ham, 1 for spam)
        """
        print(f"\nTraining {self.model_type} model...")
        
        # Preprocess texts
        X_train_processed = self.preprocess_texts(X_train)
        
        # Vectorize texts
        X_train_vec = self.vectorizer.fit_transform(X_train_processed)
        
        # Train model
        self.model.fit(X_train_vec, y_train)
        
        print(f"✓ Model trained successfully!")
        print(f"  - Vocabulary size: {len(self.vectorizer.get_feature_names_out())}")
    
    def predict(self, X_test):
        """
        Make predictions on test data
        
        Args:
            X_test: Test texts
            
        Returns:
            Predictions (0 or 1)
        """
        X_test_processed = self.preprocess_texts(X_test)
        X_test_vec = self.vectorizer.transform(X_test_processed)
        return self.model.predict(X_test_vec)
    
    def predict_proba(self, X_test):
        """Get probability predictions"""
        X_test_processed = self.preprocess_texts(X_test)
        X_test_vec = self.vectorizer.transform(X_test_processed)
        return self.model.predict_proba(X_test_vec)
    
    def evaluate(self, X_test, y_test):
        """
        Evaluate model performance
        
        Args:
            X_test: Test texts
            y_test: Test labels
            
        Returns:
            Dictionary with evaluation metrics
        """
        print(f"\nEvaluating {self.model_type} model...")
        
        y_pred = self.predict(X_test)
        
        self.metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, zero_division=0),
            'recall': recall_score(y_test, y_pred, zero_division=0),
            'f1': f1_score(y_test, y_pred, zero_division=0),
            'confusion_matrix': confusion_matrix(y_test, y_pred)
        }
        
        # Try to get ROC-AUC if probabilities are available
        try:
            y_proba = self.predict_proba(X_test)[:, 1]
            self.metrics['roc_auc'] = roc_auc_score(y_test, y_proba)
        except:
            self.metrics['roc_auc'] = None
        
        return self.metrics
    
    def print_report(self, y_test):
        """Print detailed classification report"""
        print("\n" + "="*60)
        print(f"Classification Report - {self.model_type.upper()}")
        print("="*60)
        print(f"Accuracy:  {self.metrics['accuracy']:.4f}")
        print(f"Precision: {self.metrics['precision']:.4f}")
        print(f"Recall:    {self.metrics['recall']:.4f}")
        print(f"F1-Score:  {self.metrics['f1']:.4f}")
        if self.metrics['roc_auc']:
            print(f"ROC-AUC:   {self.metrics['roc_auc']:.4f}")
        print("\nConfusion Matrix:")
        print(self.metrics['confusion_matrix'])
        print("="*60)
    
    def save_model(self, filepath):
        """Save model and vectorizer to disk"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        model_data = {
            'model': self.model,
            'vectorizer': self.vectorizer,
            'preprocessor': self.preprocessor,
            'model_type': self.model_type
        }
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"✓ Model saved to {filepath}")
    
    @staticmethod
    def load_model(filepath):
        """Load model from disk"""
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        classifier = SpamClassifier(model_type=model_data['model_type'])
        classifier.model = model_data['model']
        classifier.vectorizer = model_data['vectorizer']
        classifier.preprocessor = model_data['preprocessor']
        print(f"✓ Model loaded from {filepath}")
        return classifier


def load_kaggle_dataset():
    """
    Load SMS Spam Collection dataset from local path
    Download from: https://www.kaggle.com/uciml/sms-spam-collection-dataset
    """
    # Check if data file exists
    data_path = 'data/spam.csv'
    
    if not os.path.exists(data_path):
        print(f"\n⚠ Dataset not found at {data_path}")
        print("Download the SMS Spam Collection dataset from Kaggle:")
        print("https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset")
        print("Extract 'spam.csv' to the 'data' folder")
        return None
    
    # Load dataset
    df = pd.read_csv(data_path, encoding='latin-1')
    
    # Handle different column names in the dataset
    if 'v1' in df.columns and 'v2' in df.columns:
        df = df[['v1', 'v2']]
        df.columns = ['label', 'message']
    
    # Convert labels to binary (ham=0, spam=1)
    df['label'] = (df['label'] == 'spam').astype(int)
    
    print(f"✓ Dataset loaded: {len(df)} messages")
    print(f"  - Ham: {len(df[df['label'] == 0])}")
    print(f"  - Spam: {len(df[df['label'] == 1])}")
    
    return df


def create_sample_dataset():
    """Create a sample dataset for demonstration if Kaggle data is not available"""
    print("\nCreating sample dataset for demonstration...")
    
    ham_messages = [
        "Hey, how are you doing today?",
        "Can you send me the project files?",
        "Let's meet at 3pm tomorrow",
        "I'll call you back in an hour",
        "Thanks for the help yesterday",
        "What time is the meeting?",
        "See you at the office",
        "Happy birthday!",
        "Got your email, will respond soon",
        "The presentation looks great"
    ]
    
    spam_messages = [
        "YOU HAVE WON A FREE PRIZE!!! Claim now",
        "Click here to get free money NOW!!!",
        "Buy cheap medications online",
        "CONGRATULATIONS! You are a lucky winner",
        "FREE CASH!!! No work required",
        "Act now!!! Limited time offer",
        "Click here for amazing deals",
        "You have been selected as winner",
        "Earn $$$$ from home easily",
        "Get rich quick! Click here now!"
    ]
    
    labels = [0]*len(ham_messages) + [1]*len(spam_messages)
    messages = ham_messages + spam_messages
    
    df = pd.DataFrame({'message': messages, 'label': labels})
    df = df.sample(frac=1).reset_index(drop=True)  # Shuffle
    
    print(f"✓ Sample dataset created: {len(df)} messages")
    print(f"  - Ham: {len(df[df['label'] == 0])}")
    print(f"  - Spam: {len(df[df['label'] == 1])}")
    
    return df


def main():
    """Main function to train and evaluate the spam classifier"""
    
    print("\n" + "="*60)
    print("SPAM/HAM CLASSIFICATION MODEL")
    print("="*60)
    
    # Load dataset
    df = load_kaggle_dataset()
    if df is None:
        df = create_sample_dataset()
    
    # Display dataset statistics
    print("\nDataset Statistics:")
    print(f"Total messages: {len(df)}")
    print(f"Spam percentage: {(df['label'].sum() / len(df) * 100):.2f}%")
    
    # Split data
    X = df['message'].values
    y = df['label'].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\nData Split:")
    print(f"Training set: {len(X_train)} messages")
    print(f"Test set: {len(X_test)} messages")
    
    # Train multiple models
    models_to_train = ['naive_bayes', 'logistic_regression', 'random_forest']
    trained_models = {}
    results = []
    
    for model_type in models_to_train:
        classifier = SpamClassifier(model_type=model_type)
        classifier.train(X_train, y_train)
        metrics = classifier.evaluate(X_test, y_test)
        classifier.print_report(y_test)
        
        trained_models[model_type] = classifier
        results.append({
            'Model': model_type.replace('_', ' ').title(),
            'Accuracy': metrics['accuracy'],
            'Precision': metrics['precision'],
            'Recall': metrics['recall'],
            'F1-Score': metrics['f1'],
            'ROC-AUC': metrics['roc_auc'] if metrics['roc_auc'] else 'N/A'
        })
    
    # Display comparison
    print("\n" + "="*60)
    print("MODEL COMPARISON")
    print("="*60)
    results_df = pd.DataFrame(results)
    print(results_df.to_string(index=False))
    
    # Save best model
    best_model = trained_models['naive_bayes']
    best_model.save_model('models/spam_classifier_model.pkl')
    
    # Generate visualizations
    generate_visualizations(trained_models, X_test, y_test)
    
    print("\n✓ Training complete! Model saved to 'models/spam_classifier_model.pkl'")
    return trained_models, X_test, y_test


def generate_visualizations(models, X_test, y_test):
    """Generate visualization plots for model evaluation"""
    print("\nGenerating visualizations...")
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Spam Classification Model Evaluation', fontsize=16, fontweight='bold')
    
    # Plot 1: Confusion Matrix
    classifier = models['naive_bayes']
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    
    if sns:
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0, 0],
                    xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
    else:
        im = axes[0, 0].imshow(cm, cmap='Blues')
        axes[0, 0].set_xticks([0, 1])
        axes[0, 0].set_yticks([0, 1])
        axes[0, 0].set_xticklabels(['Ham', 'Spam'])
        axes[0, 0].set_yticklabels(['Ham', 'Spam'])
        for i in range(2):
            for j in range(2):
                axes[0, 0].text(j, i, cm[i, j], ha="center", va="center", color="w")
        plt.colorbar(im, ax=axes[0, 0])
    
    axes[0, 0].set_title('Confusion Matrix - Naive Bayes')
    axes[0, 0].set_ylabel('True Label')
    axes[0, 0].set_xlabel('Predicted Label')
    
    # Plot 2: Metrics Comparison
    metrics_names = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    model_names = list(models.keys())
    
    metrics_data = {metric: [] for metric in metrics_names}
    for model_type in model_names:
        metrics = models[model_type].metrics
        metrics_data['Accuracy'].append(metrics['accuracy'])
        metrics_data['Precision'].append(metrics['precision'])
        metrics_data['Recall'].append(metrics['recall'])
        metrics_data['F1-Score'].append(metrics['f1'])
    
    x = np.arange(len(model_names))
    width = 0.2
    
    for i, metric in enumerate(metrics_names):
        axes[0, 1].bar(x + i*width, metrics_data[metric], width, label=metric)
    
    axes[0, 1].set_xlabel('Model')
    axes[0, 1].set_ylabel('Score')
    axes[0, 1].set_title('Metrics Comparison')
    axes[0, 1].set_xticks(x + width * 1.5)
    axes[0, 1].set_xticklabels([m.replace('_', '\n') for m in model_names], fontsize=8)
    axes[0, 1].legend()
    axes[0, 1].set_ylim([0, 1])
    
    # Plot 3: Class Distribution
    unique, counts = np.unique(y_test, return_counts=True)
    axes[1, 0].pie(counts, labels=['Ham', 'Spam'], autopct='%1.1f%%',
                   colors=['#2ecc71', '#e74c3c'])
    axes[1, 0].set_title('Test Set Class Distribution')
    
    # Plot 4: ROC Curve (if available)
    try:
        classifier = models['naive_bayes']
        y_proba = classifier.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = roc_auc_score(y_test, y_proba)
        
        axes[1, 1].plot(fpr, tpr, color='darkorange', lw=2,
                       label=f'ROC curve (AUC = {roc_auc:.3f})')
        axes[1, 1].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        axes[1, 1].set_xlim([0.0, 1.0])
        axes[1, 1].set_ylim([0.0, 1.05])
        axes[1, 1].set_xlabel('False Positive Rate')
        axes[1, 1].set_ylabel('True Positive Rate')
        axes[1, 1].set_title('ROC Curve - Naive Bayes')
        axes[1, 1].legend(loc="lower right")
    except:
        axes[1, 1].text(0.5, 0.5, 'ROC Curve\nNot Available',
                       ha='center', va='center', transform=axes[1, 1].transAxes)
        axes[1, 1].set_title('ROC Curve')
    
    plt.tight_layout()
    plt.savefig('models/evaluation_plots.png', dpi=300, bbox_inches='tight')
    print("✓ Visualizations saved to 'models/evaluation_plots.png'")
    plt.close()


if __name__ == "__main__":
    trained_models, X_test, y_test = main()
