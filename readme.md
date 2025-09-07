# ML Workflow App

## Overview
The **ML Workflow App** is an interactive Streamlit application designed to guide users through a complete Machine Learning workflow:
from **data upload** and **exploration**, to **cleaning**, **feature engineering**, **train/test splitting**, and **model training & evaluation**.  
It supports both **classification** and **regression** tasks and is suitable for educational purposes or rapid prototyping.

---

## Features

### 1. Upload & Explore
- Upload CSV or Excel datasets.
- View column statistics and unique value counts.
- Visualize distributions and correlations dynamically.

### 2. Data Cleaning
- Remove nulls or unwanted values.
- Convert column types.
- Replace substrings or apply transformations.
- Rename or drop columns.
- Undo operations at any stage.

### 3. Feature Engineering
- Encode categorical variables (Label, One-Hot, Ordinal).
- Split columns by delimiter or substring.
- Extract features from text using Regex or keyword mapping.
- Preview and undo transformations.

### 4. Split Train/Test
- Select features and target column.
- Configure test size and random state.
- Submit the split and preview train/test sets.

### 5. Model Training & Evaluation
- Classification: Logistic Regression, Decision Tree, Random Forest, SVM, XGBoost.
- Regression: Linear Regression, Decision Tree Regressor, Random Forest Regressor, SVR, XGBoost Regressor.
- Dynamic evaluation metrics: accuracy, classification report, confusion matrix, MSE, R².
- Visualize predictions vs actual for regression tasks.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ml-workflow-app.git
cd ml-workflow-app
``` 
 
2. Create a virtual environment (optional but recommended): 
 
```bash 
python -m venv venv 
source venv/bin/activate  # Linux/Mac 
venv\Scripts\activate     # Windows 
``` 
 
3. Install dependencies: 
 
```bash 
pip install -r requirements.txt 
``` 
 
4. Run the app: 
 
```bash 
streamlit run Home.py 
``` 
 
--- 
 
## Notes 
 
* For XGBoost models, ensure `xgboost` is installed. 
* Always check your target column for nulls before splitting. 
* Use the **Undo** feature to revert transformations. 
 
--- 
 