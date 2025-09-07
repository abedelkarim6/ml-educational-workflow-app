# Home.py
import streamlit as st

st.set_page_config(page_title="ML Workflow App", page_icon="🤖", layout="wide")

st.title("🤖 ML Workflow App")
st.markdown(
    """
Welcome to the **ML Workflow App**, your interactive tool to explore, clean, engineer features, 
split datasets, train models, and evaluate performance — all in a single Streamlit application.  
This platform is designed for both beginners and advanced users in **Data Science & Machine Learning**.

---

### 🔹 Features Overview

1. **Upload & Explore**
   - Upload CSV or Excel files.
   - View summary statistics and value counts.
   - Visualize data distributions and correlations with dynamic plots.

2. **Data Cleaning**
   - Remove nulls or unwanted values.
   - Convert columns to numeric types.
   - Replace substrings or apply transformations.
   - Rename columns and drop irrelevant ones.
   - Undo operations at any time.

3. **Feature Engineering**
   - Encode categorical variables (Label, One-Hot, Ordinal).
   - Split columns by delimiter or substring.
   - Extract structured features from text (Regex, Keyword Mapping).
   - Preview column values and undo changes.

4. **Split Train/Test**
   - Choose target and feature columns.
   - Configure test size and random state.
   - Submit split with preview of training/testing sets.

5. **Model Training & Evaluation**
   - Classification: Logistic Regression, Decision Tree, Random Forest, SVM, XGBoost.
   - Regression: Linear Regression, Decision Tree Regressor, Random Forest Regressor, SVR, XGBoost Regressor.
   - View metrics dynamically: accuracy, confusion matrix, MSE, R².
   - Visualize predictions vs actual for regression tasks.

---

### 🔹 Navigation
Use the sidebar to navigate between pages:

- **📂 Upload & Explore** – Upload your dataset and inspect it.
- **⚙️ Data Cleaning** – Clean and preprocess your data.
- **🧩 Feature Engineering** – Transform and create features.
- **📊 Split Train/Test** – Split your dataset into training/testing sets.
- **🤖 Model Training & Evaluation** – Train models and evaluate performance.

---

### 🔹 Tips
- Always inspect your target column for nulls before splitting.
- Use regex carefully in feature extraction; preview the output first.
- Undo operations to correct mistakes at any stage.

---

Enjoy building and testing your Machine Learning workflows interactively!
"""
)
