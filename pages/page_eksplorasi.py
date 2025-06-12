import streamlit as st
import pandas as pd

def show_eksplorasi():
    st.title("📊 Eksplorasi Dataset Kelulusan Mahasiswa")

    df = pd.read_csv("data/dataset_kelulusan_mahasiswa.csv")

    st.subheader("Cuplikan Data")
    st.dataframe(df.head())

    st.subheader("Statistik Deskriptif")
    st.write(df.describe())

    st.subheader("Informasi Tipe Data")
    buffer = df.dtypes.astype(str)
    st.write(buffer)
