"""
Setup script for Spam/Ham Classification Project
"""

import os
import sys

def create_data_folder():
    """Create data folder and provide instructions for dataset"""
    os.makedirs('data', exist_ok=True)
    
    instructions = """
    =================================================================
    DATASET SETUP INSTRUCTIONS
    =================================================================
    
    To use the SMS Spam Collection dataset from Kaggle:
    
    1. Go to: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
    2. Download the 'spam.csv' file
    3. Place it in the 'data' folder of this project
    4. Run the spam_classifier.py script
    
    If you don't have Kaggle account/don't want to download:
    - The script will automatically create a sample dataset for demonstration
    
    =================================================================
    """
    
    print(instructions)
    
    # Create a placeholder file
    with open('data/README.txt', 'w') as f:
        f.write(instructions)

if __name__ == '__main__':
    print("\nSetting up Spam/Ham Classification Project...")
    create_data_folder()
    print("✓ Setup complete!")
    print("\nNext steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Download dataset and place in 'data' folder")
    print("3. Run: python src/spam_classifier.py")
