import streamlit as st
import pandas as pd
import numpy as np

def show_prediksi():
    st.title(" Prediksi Kelulusan Mahasiswa")

    st.write("Silakan masukkan nilai berikut untuk memprediksi kelulusan:")

    umur = st.number_input("Umur", 17, 40, 21)
    ipk = st.slider("IPK", 0.0, 4.0, 2.5)
    sks = st.number_input("Jumlah SKS", 0, 160, 100)

    if st.button("Prediksi"):
        pred = "Lulus" if ipk >= 2.75 and sks > 110 else "Tidak Lulus"
        st.success(f"Hasil Prediksi: {pred}")
