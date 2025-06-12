import streamlit as st

st.set_page_config(page_title="Dashboard Kelulusan Mahasiswa", layout="wide")

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Eksplorasi Dataset", "Performa Model", "Prediksi"])

if page == "Eksplorasi Dataset":
    from pages.page_eksplorasi import show_eksplorasi
    show_eksplorasi()
elif page == "Performa Model":
    from pages.page_performa import show_performa
    show_performa()
elif page == "Prediksi":
    from pages.page_prediksi import show_prediksi
    show_prediksi()
