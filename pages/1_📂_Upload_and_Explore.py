import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📂 Upload & Explore Data")


# --- Cache loading function ---
@st.cache_data
def load_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)


# --- File upload ---
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

# --- Load if uploaded or reuse previous session state ---
if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.session_state["df"] = df
elif "df" in st.session_state:
    df = st.session_state["df"]
else:
    df = None

# --- Exploration section ---
if df is not None:
    st.subheader("Preview Data")
    st.dataframe(df.head())

    st.subheader("Dataset Info")
    st.write("Shape:", df.shape)
    st.write(df.dtypes)

    st.subheader("Descriptive Statistics")
    st.write(df.describe(include="all"))

    st.subheader("Correlation Heatmap")
    numeric_df = df.select_dtypes(include=["float64", "int64"])
    if not numeric_df.empty:
        corr = numeric_df.corr()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.info("No numeric columns available for correlation heatmap.")

    # --- Column Exploration ---
    st.subheader("🔎 Explore a Column")
    col = st.selectbox("Choose a column to explore", df.columns)

    if col:
        st.write(f"### Distribution of `{col}`")

        if pd.api.types.is_numeric_dtype(df[col]):
            fig, ax = plt.subplots()
            sns.histplot(df[col].dropna(), bins=20, kde=True, ax=ax)
            st.pyplot(fig)
        else:
            vc = df[col].value_counts().head(20)  # show top 20
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.barplot(x=vc.index.astype(str), y=vc.values, ax=ax)
            ax.set_ylabel("Count")
            ax.set_xlabel(col)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)

# if uploaded_file:
#     if uploaded_file.name.endswith(".csv"):
#         df = pd.read_csv(uploaded_file)
#     else:
#         df = pd.read_excel(uploaded_file)

#     st.session_state["df"] = df

#     st.subheader("Preview Data")
#     st.dataframe(df.head())

#     st.subheader("Dataset Info")
#     st.write("Shape:", df.shape)
#     st.write(df.dtypes)

#     st.subheader("Descriptive Statistics")
#     st.write(df.describe(include="all"))

#     st.subheader("Correlation Heatmap")
#     numeric_df = df.select_dtypes(include=["float64", "int64"])

#     if numeric_df.shape[1] >= 2:  # at least 2 numeric columns
#         corr = numeric_df.corr()
#         fig, ax = plt.subplots(figsize=(8, 5))
#         sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
#         st.pyplot(fig)
#     elif numeric_df.shape[1] == 1:
#         st.info(
#             "Only one numeric column available — correlation heatmap requires at least 2."
#         )
#     else:
#         st.info("No numeric columns available for correlation heatmap.")
