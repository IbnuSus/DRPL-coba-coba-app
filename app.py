import streamlit as st
import pandas as pd

# Judul Dashboard
st.title("Dashboard Penjualan Produk Digital 🚀")
st.write("Ini adalah dashboard percobaan pertama. Kalau yang ini muncul, berarti kamu sudah berhasil deploy!")

# 1. Membuat data buatan sederhana
data = {
    'Nama Produk': ['E-book Bisnis', 'Tiket Webinar', 'Template Web', 'Konsultasi Online'],
    'Jumlah Terjual': [120, 85, 200, 40]
}
df = pd.DataFrame(data)

# 2. Menampilkan tabel data
st.subheader("Tabel Data Penjualan")
st.dataframe(df)

# 3. Menampilkan grafik bawaan Streamlit (Tanpa Matplotlib/Seaborn agar tidak error)
st.subheader("Grafik Penjualan")
# Mengatur 'Nama Produk' sebagai index agar nama produknya muncul di bagian bawah grafik
st.bar_chart(df.set_index('Nama Produk'))

# 4. Fitur Interaktif sederhana
st.subheader("Fitur Interaktif")
pilihan = st.selectbox("Pilih produk yang ingin disorot:", df['Nama Produk'])

st.success(f"Sistem berjalan lancar! Kamu sedang memilih: **{pilihan}**")