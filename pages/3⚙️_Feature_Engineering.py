import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

# --- Initialize history ---
if "df" not in st.session_state or st.session_state.df is None:
    st.warning("Please upload a dataset first in the Upload page.")
else:
    if "history" not in st.session_state:
        st.session_state.history = []

    st.title("🔧 Feature Engineering")

    df = st.session_state.df.copy()

    # --- Preview Data Section ---
    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    selected_col = st.selectbox("Select a column to preview values", df.columns)
    if selected_col:
        if df[selected_col].dtype == "object":
            st.write(df[selected_col].value_counts().head(10))
        else:
            st.write(df[selected_col].describe())

    st.markdown("---")

    # --- Encoding Section ---
    st.subheader("Categorical Encoding")

    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if cat_cols:
        col_to_encode = st.selectbox(
            "Select a column to encode", cat_cols, key="encode_col"
        )
        encoding_method = st.radio(
            "Choose encoding method",
            ["Label Encoding", "One-Hot Encoding", "Ordinal Encoding"],
        )

        if st.button("Apply Encoding"):
            # Save history
            st.session_state.history.append(df.copy())

            if encoding_method == "Label Encoding":
                le = LabelEncoder()
                df[col_to_encode + "_encoded"] = le.fit_transform(df[col_to_encode])
                st.success(f"Applied Label Encoding on {col_to_encode}")

            elif encoding_method == "One-Hot Encoding":
                df = pd.get_dummies(df, columns=[col_to_encode], prefix=col_to_encode)
                st.success(f"Applied One-Hot Encoding on {col_to_encode}")

            elif encoding_method == "Ordinal Encoding":
                oe = OrdinalEncoder()
                df[col_to_encode + "_ordinal"] = oe.fit_transform(df[[col_to_encode]])
                st.success(f"Applied Ordinal Encoding on {col_to_encode}")

            st.session_state.df = df
            st.dataframe(df.head())
    else:
        st.info("No categorical columns available for encoding.")

    st.markdown("---")

    # --- Split Column Section ---
    st.subheader("Split Column by Substring")

    split_col = st.selectbox("Select a column to split", df.columns, key="split_col")
    delimiter = st.text_input("Enter delimiter (substring to split on)", ",")

    if st.button("Split Column"):
        try:
            # Save history
            st.session_state.history.append(df.copy())

            new_cols = df[split_col].astype(str).str.split(delimiter, n=1, expand=True)
            if new_cols.shape[1] == 2:
                df[split_col + "_part1"] = new_cols[0]
                df[split_col + "_part2"] = new_cols[1]
                st.success(f"Split {split_col} into two new columns.")
                st.session_state.df = df
                st.dataframe(df.head())
            else:
                st.error("Could not split column into 2 parts. Check delimiter.")
        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown("---")

    # --- Undo Option ---
    if st.button("Undo Last Operation"):
        if st.session_state.history:
            st.session_state.df = st.session_state.history.pop()
            st.success("Undid last operation.")
            st.dataframe(st.session_state.df.head())
        else:
            st.info("No operations to undo.")

st.subheader("🔧 Advanced Feature Extraction from Text Columns")

text_cols = df.select_dtypes(include=["object"]).columns.tolist()
if text_cols:
    col_to_extract = st.selectbox(
        "Select a text column", text_cols, key="text_col_extract"
    )

    extraction_method = st.radio(
        "Select extraction method",
        ["Regex Extract", "Split by Delimiter", "Keyword Mapping"],
        key="extract_method",
    )

    if extraction_method == "Regex Extract":
        # Regex tips expander
        with st.expander("💡 Regex Tips & Examples"):
            st.markdown(
                """
            - Use parentheses `()` to create **groups** → each group becomes a new column.
            - Example 1: Extract CPU GHz from `"Intel Core i5 1.8GHz"` → `(\\d+\\.\\d)` → 1.8
            - Example 2: Extract resolution from `"2880x1800"` → `(\\d+)x(\\d+)` → width=2880, height=1800
            - Example 3: Extract GPU model from `"Intel HD Graphics 620"` → `(\d+)$` → 620
            - Test your regex online: [https://regex101.com/](https://regex101.com/)
            """
            )

        regex_pattern = st.text_input(
            "Enter regex pattern (use groups for new columns)", key="regex_pattern"
        )
        new_col_names = st.text_input(
            "Enter new column names separated by comma", key="regex_new_cols"
        )
        new_col_names = [x.strip() for x in new_col_names.split(",")]

        if st.button("Apply Regex Extraction", key="regex_extract_btn"):
            try:
                st.session_state.history.append(df.copy())
                matches = df[col_to_extract].str.extract(regex_pattern)
                if matches.shape[1] != len(new_col_names):
                    st.error(
                        "Number of groups does not match number of new column names"
                    )
                else:
                    matches.columns = new_col_names
                    df = pd.concat([df, matches], axis=1)
                    st.session_state.df = df
                    st.success("Regex extraction applied!")
                    st.dataframe(df.head())
            except Exception as e:
                st.error(f"Error: {e}")
