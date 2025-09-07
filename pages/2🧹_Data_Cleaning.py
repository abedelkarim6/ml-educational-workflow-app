import streamlit as st
import pandas as pd

st.title("🧹 Data Cleaning")

if "df" not in st.session_state:
    st.warning("Please upload data first.")
else:
    df = st.session_state["df"].copy()

    st.write("### Current DataFrame Preview")
    st.dataframe(df.head())

    col = st.selectbox("Select a column to clean:", df.columns)

    if col:
        st.write(f"Cleaning options for **{col}**")

        action = st.radio(
            "Choose an action",
            [
                "Do nothing",
                "Remove Nulls",
                "Fill Nulls (Mean/Median/Mode)",
                "Remove Specific Values",
                "Convert to Numeric",
                "Convert to String",
                "Drop Column",
                "Replace Substring",
                "Apply Operation to Values",
                "Rename Column",
            ],
        )

        apply_btn = st.button("✅ Apply Operation on Column")

        if apply_btn:
            if action == "Remove Nulls":
                # df[col] = df[col].dropna()
                df = df[df[col].notnull()]

            elif action == "Fill Nulls (Mean/Median/Mode)":
                method = st.selectbox("Method", ["Mean", "Median", "Mode"])
                if method == "Mean" and pd.api.types.is_numeric_dtype(df[col]):
                    df[col] = df[col].fillna(df[col].mean())
                elif method == "Median" and pd.api.types.is_numeric_dtype(df[col]):
                    df[col] = df[col].fillna(df[col].median())
                else:
                    df[col] = df[col].fillna(df[col].mode()[0])

            elif action == "Remove Specific Values":
                unique_vals = df[col].unique().tolist()
                vals_to_remove = st.multiselect("Select values to remove:", unique_vals)
                if vals_to_remove:
                    df = df[~df[col].isin(vals_to_remove)]

            elif action == "Convert to Numeric":
                df[col] = pd.to_numeric(df[col], errors="coerce")

            elif action == "Convert to String":
                df[col] = df[col].astype(str)

            elif action == "Drop Column":
                df = df.drop(columns=[col])
                st.success(f"Column **{col}** has been dropped!")

            elif action == "Replace Substring":
                old = st.text_input("Substring to replace (e.g., ',')", ",")
                new = st.text_input("Replace with (e.g., '')", "")
                if old:
                    df[col] = df[col].astype(str).str.replace(old, new, regex=False)
                    st.success(f"Replaced '{old}' with '{new}' in column {col}")

            elif action == "Apply Operation to Values":
                operation = st.text_input(
                    "Enter operation (use `x` as the value). Example: x * 0.001"
                )
                if operation:
                    try:
                        df[col] = df[col].apply(lambda x: eval(operation, {"x": x}))
                        st.success(f"Applied operation `{operation}` on column {col}")
                    except Exception as e:
                        st.error(f"Error applying operation: {e}")

            elif action == "Rename Column":
                new_name = st.text_input("Enter new column name", col)
                if new_name:
                    df = df.rename(columns={col: new_name})
                    st.success(f"Column **{col}** renamed to **{new_name}**")

            st.session_state["df"] = df

    st.subheader("Updated DataFrame")
    st.dataframe(st.session_state["df"].head())
