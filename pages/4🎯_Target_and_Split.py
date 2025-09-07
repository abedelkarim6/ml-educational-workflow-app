import streamlit as st
from sklearn.model_selection import train_test_split

if "df" not in st.session_state or st.session_state.df is None:
    st.warning("Please upload data first.")
else:
    st.title("📊 Split Train/Test")

    df = st.session_state.df.copy()

    # Select target variable
    target_col = st.selectbox("Select target column", df.columns)

    # Select features (optional)
    feature_cols = st.multiselect(
        "Select feature columns (default: all except target)",
        [c for c in df.columns if c != target_col],
    )

    # Test size
    test_size = st.slider(
        "Test set proportion", min_value=0.1, max_value=0.5, value=0.2
    )

    # Random state
    random_state = st.number_input(
        "Random state (for reproducibility)", value=42, step=1
    )

    # --- Submit Button ---
    if st.button("Submit Split", key="submit_split_btn"):
        try:
            X = df[feature_cols] if feature_cols else df.drop(columns=[target_col])
            y = df[target_col]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )

            # Save in session state
            st.session_state["X_train"] = X_train
            st.session_state["X_test"] = X_test
            st.session_state["y_train"] = y_train
            st.session_state["y_test"] = y_test

            st.success("Train/Test split completed!")
            st.write("X_train shape:", X_train.shape)
            st.write("X_test shape:", X_test.shape)
            st.write("y_train shape:", y_train.shape)
            st.write("y_test shape:", y_test.shape)

        except Exception as e:
            st.error(f"Error splitting data: {e}")
