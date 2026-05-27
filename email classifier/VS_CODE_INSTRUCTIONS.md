# How to Run in VS Code

## 🎯 QUICKEST METHOD (In VS Code Terminal)

### **Step 1: Open Terminal in VS Code**
1. Press `Ctrl + `` (backtick) to open terminal
   - OR go to **Terminal → New Terminal** from menu
   - OR press `Ctrl + Shift + ``

### **Step 2: Run Training Script**
```bash
python src/spam_classifier.py
```

**That's it!** You'll see output like:
```
============================================================
SPAM/HAM CLASSIFICATION MODEL
============================================================

Creating sample dataset for demonstration...
✓ Sample dataset created: 20 messages
...
✓ Training complete! Model saved to 'models/spam_classifier_model.pkl'
```

---

## 📋 DETAILED VS CODE INSTRUCTIONS

### **Method 1: Using Integrated Terminal (RECOMMENDED)**

1. **Open the folder** in VS Code:
   - File → Open Folder
   - Select: `C:\Users\GANESAN\Documents\email classifier`

2. **Open Terminal**:
   - Press `Ctrl + `` (or Ctrl + Shift + `)
   - OR Terminal menu → New Terminal

3. **Run any command**:
   ```bash
   # Train the model
   python src/spam_classifier.py
   
   # Make predictions
   python predict_example.py
   
   # Generate documentation
   python generate_documentation.py
   ```

---

### **Method 2: Run Configuration (VS Code Task)**

1. **Create/Open Tasks**:
   - Press `Ctrl + Shift + B` (Run Build Task)
   - OR Terminal → Run Task

2. **Select or create task**:
   - Choose "Train Spam Classifier"
   - Model starts training in terminal

---

### **Method 3: Click-to-Run (Python Extension)**

1. **Install Python Extension** (if not installed):
   - Go to Extensions (Ctrl + Shift + X)
   - Search "Python"
   - Install Microsoft's Python extension

2. **Open** `src/spam_classifier.py`

3. **Click** ▶ (Run Button) in top-right corner

---

## 🎬 STEP-BY-STEP IN VS CODE

### **Step 1: Open Project**
```
File → Open Folder → Select "email classifier" folder
```

### **Step 2: Open Terminal**
```
Press: Ctrl + `
```

### **Step 3: Run Training**
```
Type: python src/spam_classifier.py
Press: Enter
```

### **Step 4: Watch Results**
Terminal shows real-time output:
- ✓ Model training progress
- ✓ Evaluation metrics
- ✓ Model saved confirmation
- ✓ Plots generated

### **Step 5: View Generated Files**
In VS Code file explorer, you'll see new files:
- `models/spam_classifier_model.pkl` ← Trained model
- `models/evaluation_plots.png` ← Plots
- `SPAM_CLASSIFICATION_PROJECT_REPORT.docx` ← Report

---

## 📸 TERMINAL OUTPUT YOU'LL SEE

```
PS C:\Users\GANESAN\Documents\email classifier> python src/spam_classifier.py

============================================================
SPAM/HAM CLASSIFICATION MODEL
============================================================

Creating sample dataset for demonstration...
✓ Sample dataset created: 20 messages
  - Ham: 10
  - Spam: 10

Dataset Statistics:
Total messages: 20
Spam percentage: 50.00%

Data Split:
Training set: 16 messages
Test set: 4 messages

Training naive_bayes model...
✓ Model trained successfully!
  - Vocabulary size: 6

Evaluating naive_bayes model...

============================================================
Classification Report - NAIVE_BAYES
============================================================
Accuracy:  0.7500
Precision: 1.0000
Recall:    0.5000
F1-Score:  0.6667
ROC-AUC:   0.7500
============================================================

✓ Model saved to models/spam_classifier_model.pkl
✓ Visualizations saved to 'models/evaluation_plots.png'

✓ Training complete! Model saved to 'models/spam_classifier_model.pkl'
```

---

## 🔄 MULTIPLE COMMANDS IN VS CODE

### **Command 1: Train Model**
```bash
python src/spam_classifier.py
```

### **Command 2: Make Predictions**
```bash
python predict_example.py
```

### **Command 3: Generate Word Document**
```bash
python generate_documentation.py
```

**Run each in separate terminal windows:**
- Terminal 1: `Ctrl + Shift + ``
- Terminal 2: `Ctrl + Shift + ``
- Or reuse same terminal by pressing Enter after command completes

---

## 📂 VS CODE FILE EXPLORER VIEW

Your project should look like:
```
📁 email classifier
  ├── 📁 data
  ├── 📁 models
  │   ├── spam_classifier_model.pkl
  │   └── evaluation_plots.png
  ├── 📁 src
  │   └── spam_classifier.py
  ├── .gitignore
  ├── generate_documentation.py
  ├── predict_example.py
  ├── README.md
  ├── QUICKSTART.md
  ├── requirements.txt
  ├── setup.py
  └── SPAM_CLASSIFICATION_PROJECT_REPORT.docx
```

---

## ⚡ KEYBOARD SHORTCUTS

| Shortcut | Action |
|----------|--------|
| `Ctrl + `` | Open/Close Terminal |
| `Ctrl + Shift + `` | New Terminal |
| `Ctrl + Shift + B` | Run Build Task |
| `Ctrl + F5` | Run Python File |
| `F5` | Start Debugging |
| `Ctrl + K Ctrl + O` | Open Folder |

---

## 🐛 TROUBLESHOOTING IN VS CODE

### **"Python command not found"**
1. Open Command Palette: `Ctrl + Shift + P`
2. Type: "Python: Select Interpreter"
3. Choose Python 3.x version

### **"Module not found"**
1. Open Terminal: `Ctrl + ``
2. Run: `pip install -r requirements.txt`

### **Can't see files**
1. Go to File Explorer (Ctrl + Shift + E)
2. Click "Open Folder"
3. Select "email classifier"

### **Terminal not showing**
1. Press `Ctrl + ``
2. If still hidden: Terminal → New Terminal

---

## 📌 QUICK REFERENCE

**To run in VS Code terminal:**

```
1. Press Ctrl + `
2. Type: python src/spam_classifier.py
3. Press Enter
4. Wait for ✓ completion
```

That's all! Everything will run and display in the integrated terminal.

---

## 🎯 NEXT STEPS

1. ✅ Open folder in VS Code
2. ✅ Open terminal (Ctrl + `)
3. ✅ Run: `python src/spam_classifier.py`
4. ✅ View results in terminal
5. ✅ Check `models/` folder for generated files
6. ✅ View `SPAM_CLASSIFICATION_PROJECT_REPORT.docx` for report

**It's that simple!** 🚀
