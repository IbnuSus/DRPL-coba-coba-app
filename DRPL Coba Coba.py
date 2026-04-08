DRPL Coba Coba


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Mengatur judul halaman web
st.title("Dashboard Analisis Data Aplikasi - Kelompok X")
st.write("Selamat datang di dashboard interaktif hasil kerja kelompok kami!")

# 2. Membuat data buatan/dummy (Nanti kamu gunakan data asli dari tim Data Engineer)
data = {
    'Kategori Sentimen': ['Positif', 'Netral', 'Negatif'],
    'Jumlah Ulasan': [150, 45, 25]
}
df = pd.DataFrame(data)

# 3. Menampilkan tabel data di web
st.subheader("Tabel Ringkasan Ulasan")
st.dataframe(df)

# 4. Memasukkan Grafik (Biasanya kodenya dibuat oleh Data Analyst timmu)
st.subheader("Grafik Bar: Demografi Sentimen")
fig, ax = plt.subplots()
sns.barplot(x='Kategori Sentimen', y='Jumlah Ulasan', data=df, ax=ax, palette='viridis')

# Menampilkan grafik yang sudah dibuat ke dalam Streamlit
st.pyplot(fig)

# 5. Mengaktifkan Widget Interaktif (Tugas khusus DevOps/Dashboard Dev)
st.subheader("Filter Data Interaktif")
pilihan = st.selectbox("Pilih kategori ulasan untuk melihat detail:", ['Semua', 'Positif', 'Netral', 'Negatif'])

if pilihan != 'Semua':
    st.write(f"Kamu memfilter data untuk ulasan: **{pilihan}**")
else:
    st.write("Menampilkan semua data.")