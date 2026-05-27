"""
Example script to use the trained spam classifier for predictions
"""

import sys
sys.path.insert(0, 'src')
from spam_classifier import SpamClassifier

def predict_messages():
    """Predict if messages are spam or ham"""
    
    print("\n" + "="*60)
    print("SPAM/HAM PREDICTION EXAMPLE")
    print("="*60)
    
    # Load the trained model
    print("\nLoading trained model...")
    classifier = SpamClassifier.load_model('models/spam_classifier_model.pkl')
    
    # Example messages
    test_messages = [
        "Hi, can you call me back?",  # Ham
        "CONGRATULATIONS! You won a prize! Click here now!!!",  # Spam
        "The meeting is scheduled for tomorrow at 10am",  # Ham
        "Buy cheap medications online - LIMITED TIME!!!",  # Spam
        "Thanks for your help with the project",  # Ham
    ]
    
    print("\nMaking predictions on test messages:\n")
    
    for message in test_messages:
        prediction = classifier.predict([message])[0]
        proba = classifier.predict_proba([message])[0]
        
        label = "SPAM" if prediction == 1 else "HAM"
        confidence = max(proba) * 100
        
        print(f"Message: \"{message}\"")
        print(f"Prediction: {label} (Confidence: {confidence:.2f}%)")
        print(f"Probabilities - Ham: {proba[0]:.4f}, Spam: {proba[1]:.4f}")
        print("-" * 60)

if __name__ == "__main__":
    predict_messages()
