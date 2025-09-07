import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    mean_squared_error,
    r2_score,
)

# Optional: XGBoost
try:
    from xgboost import XGBClassifier, XGBRegressor

    xgb_available = True
except:
    xgb_available = False

st.title("🤖 Model Training & Evaluation")

# Check if data is ready
if "X_train" not in st.session_state:
    st.warning("Please split the data first.")
else:
    X_train, X_test = st.session_state["X_train"], st.session_state["X_test"]
    y_train, y_test = st.session_state["y_train"], st.session_state["y_test"]

    # Ask user whether it's classification or regression
    task_type = st.radio("Task Type", ["Classification", "Regression"], index=0)

    # Models per task
    if task_type == "Classification":
        models = ["Logistic Regression", "Decision Tree", "Random Forest", "SVM"]
        if xgb_available:
            models.append("XGBoost")
    else:
        models = [
            "Linear Regression",
            "Decision Tree Regressor",
            "Random Forest Regressor",
            "SVM Regressor",
        ]
        if xgb_available:
            models.append("XGBoost Regressor")

    model_choice = st.selectbox("Choose Model", models)

    if st.button("Train Model", key="train_model_btn"):
        # Initialize model
        if model_choice == "Logistic Regression":
            model = LogisticRegression(max_iter=500)
        elif model_choice == "Decision Tree":
            model = DecisionTreeClassifier()
        elif model_choice == "Random Forest":
            model = RandomForestClassifier()
        elif model_choice == "SVM":
            model = SVC()
        elif model_choice == "Linear Regression":
            model = LinearRegression()
        elif model_choice == "Decision Tree Regressor":
            model = DecisionTreeRegressor()
        elif model_choice == "Random Forest Regressor":
            model = RandomForestRegressor()
        elif model_choice == "SVM Regressor":
            model = SVR()
        elif model_choice == "XGBoost":
            model = XGBClassifier()
        elif model_choice == "XGBoost Regressor":
            model = XGBRegressor()
        else:
            st.error("Unknown model")
            st.stop()

        # Train model
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        st.subheader("Evaluation Metrics")
        if task_type == "Classification":
            st.write("Accuracy:", accuracy_score(y_test, y_pred))
            st.text("Classification Report:\n" + classification_report(y_test, y_pred))

            st.subheader("Confusion Matrix")
            cm = confusion_matrix(y_test, y_pred)
            fig, ax = plt.subplots()
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
            st.pyplot(fig)

        else:  # Regression
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            st.write(f"Mean Squared Error: {mse:.4f}")
            st.write(f"R² Score: {r2:.4f}")

            st.subheader("Prediction vs Actual Plot")
            fig, ax = plt.subplots()
            ax.scatter(y_test, y_pred, alpha=0.7)
            ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
            ax.set_xlabel("Actual")
            ax.set_ylabel("Predicted")
            st.pyplot(fig)
