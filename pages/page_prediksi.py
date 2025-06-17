import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Load model
@st.cache_data
def load_model():
    with open("model/model_kelulusan.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

def show_prediksi():
    st.title("🎓 Prediksi Kelulusan Mahasiswa")

    st.subheader("Masukkan Data Mahasiswa")

    # Input dari pengguna
    ipk = st.slider("IPK", min_value=0.0, max_value=4.0, step=0.01, value=3.0)
    ips = st.slider("IPS Terakhir", min_value=0.0, max_value=4.0, step=0.01, value=3.0)
    tidak_lulus = st.slider("Jumlah Mata Kuliah Tidak Lulus", 0, 10, 0)
    bekerja = st.selectbox("Apakah Mahasiswa Bekerja?", ("Tidak", "Ya"))
    kehadiran = st.slider("Persentase Kehadiran (%)", 0, 100, 85)

    # Konversi input ke format model
    input_data = np.array([[
        ipk,
        ips,
        tidak_lulus,
        1 if bekerja == "Ya" else 0,
        kehadiran
    ]])

    # Tombol prediksi
    if st.button("Prediksi"):
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)

        # Hasil prediksi
        st.subheader("Hasil Prediksi")
        if prediction[0] == 1:
            st.success("### Mahasiswa diprediksi **LULUS** 🎉")
            st.write(f"Probabilitas: {probability[0][1]*100:.2f}%")
        else:
            st.error("### Mahasiswa diprediksi **TIDAK LULUS** ❌")
            st.write(f"Probabilitas: {probability[0][0]*100:.2f}%")

        # Visualisasi probabilitas
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.barh(['Tidak Lulus', 'Lulus'], probability[0], color=['#ff6b6b', '#51cf66'])
        ax.set_xlim(0, 1)
        ax.set_xlabel('Probabilitas')
        ax.set_title('Probabilitas Kelulusan')
        st.pyplot(fig)

        # Rekomendasi
        st.subheader("Rekomendasi")
        if prediction[0] == 0:
            st.write("""
            Berdasarkan prediksi, mahasiswa memiliki risiko tidak lulus. Berikut rekomendasi:
            - **Tingkatkan IPK dan IPS**: Fokus belajar pada mata kuliah inti
            - **Kurangi jumlah mata kuliah tidak lulus**
            - **Perbaiki kehadiran**
            - **Jika bekerja, atur ulang manajemen waktu**
            """)
        else:
            st.write("""
            Mahasiswa diprediksi lulus. Tetap pertahankan performa:
            - **Pertahankan IPK dan IPS**
            - **Jaga konsistensi kehadiran**
            - **Fokus pada penyelesaian tugas akhir**
            """)
