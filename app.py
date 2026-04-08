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

import streamlit as st
import pandas as pd

st.title("Belajar Menampilkan Tabel 📊")

# 1. Kita buat data bohong-bohongan dulu (sebagai pengganti data dari Data Engineer)
data_ulasan = {
    "Nama Pengguna": ["Budi", "Siti", "Andi", "Rina", "Joko"],
    "Rating": [5, 4, 1, 3, 5],
    "Komentar": ["Aplikasi mantap!", "Bagus, tapi agak lemot", "Sering error pas login", "Lumayan lah", "Sangat membantu tugas kuliah"]
}

# 2. Ubah data biasa di atas menjadi format tabel resmi (disebut DataFrame) menggunakan Pandas
df = pd.DataFrame(data_ulasan)

# --- CARA 1: st.dataframe() ---
st.subheader("Cara 1: Tabel Interaktif (st.dataframe)")
st.write("Coba arahkan mouse ke tabel ini. Kamu bisa klik nama kolom (misal klik 'Rating') untuk mengurutkan angka dari kecil ke besar, dan kalau datanya banyak, tabel ini bisa di-scroll!")
st.dataframe(df)

st.divider() # Ini untuk membuat garis pembatas horizontal

# --- CARA 2: st.table() ---
st.subheader("Cara 2: Tabel Statis (st.table)")
st.write("Kalau yang ini bentuknya kaku. Semua data langsung digelar ke bawah tanpa bisa di-scroll atau diurutkan. Cocok untuk data ringkasan yang cuma 3-5 baris.")
st.table(df)

import streamlit as st
import pandas as pd

st.title("Belajar Membuat Diagram 📈")
st.write("Berikut adalah contoh 3 jenis diagram yang sering dipakai dalam dashboard.")

# --- DATA UNTUK GRAFIK BATANG & GARIS ---
# Kita buat data tren ulasan per bulan
data_tren = pd.DataFrame({
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei"],
    "Jumlah Ulasan": [20, 50, 80, 150, 200]
})
# Mengubah kolom 'Bulan' menjadi index agar tulisan bulannya ada di bawah grafik
data_tren = data_tren.set_index("Bulan")


# --- 1. DIAGRAM BATANG (BAR CHART) ---
st.subheader("1. Diagram Batang (Bar Chart)")
st.write("Sangat mudah pakai fitur bawaan Streamlit. Cocok untuk membandingkan jumlah.")
st.bar_chart(data_tren)


# --- 2. DIAGRAM GARIS (LINE CHART) ---
st.subheader("2. Diagram Garis (Line Chart)")
st.write("Sama mudahnya dengan bar chart. Cocok untuk melihat tren naik-turun dari waktu ke waktu.")
st.line_chart(data_tren)

st.divider()

# --- 3. DIAGRAM LINGKARAN (PIE CHART) ---
st.subheader("3. Diagram Lingkaran (Pie Chart)")
st.write("Streamlit tidak punya fitur pie chart bawaan, jadi kita menggunakan Matplotlib. Nanti, kodenya mirip seperti yang akan dibuat oleh teman Data Analyst-mu!")

# Data khusus untuk Pie Chart
kategori = ['Positif', 'Netral', 'Negatif']
jumlah = [120, 30, 50]
warna = ['#4CAF50', '#FFC107', '#F44336'] # Warna: Hijau, Kuning, Merah

# Kode membuat Pie Chart (Biasanya ini jatah Data Analyst)




import streamlit as st
import pandas as pd



st.title("Diagram Batang (Bar Chart) 📊")

# Menyiapkan data
data_tren = pd.DataFrame({
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei"],
    "Jumlah Ulasan": [20, 50, 80, 150, 200]
})

# Menjadikan 'Bulan' sebagai patokan (index) sumbu X di bawah grafik
data_tren = data_tren.set_index("Bulan")

# Menampilkan grafik batang
st.bar_chart(data_tren)

import streamlit as st
import pandas as pd

st.title("Diagram Garis (Line Chart) 📈")

# Menyiapkan data
data_tren = pd.DataFrame({
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei"],
    "Jumlah Ulasan": [20, 50, 80, 150, 200]
})

# Menjadikan 'Bulan' sebagai patokan (index) sumbu X di bawah grafik
data_tren = data_tren.set_index("Bulan")

# Menampilkan grafik garis
st.line_chart(data_tren)

import streamlit as st


st.title("Diagram Lingkaran (Pie Chart) 🥧")

# Menyiapkan data
kategori = ['Positif', 'Netral', 'Negatif']
jumlah = [120, 30, 50]
warna = ['#4CAF50', '#FFC107', '#F44336'] # Hijau, Kuning, Merah

# Membuat bentuk Pie Chart menggunakan Matplotlib


# Menampilkan gambar yang sudah dibuat ke layar Streamlit

import streamlit as st
import pandas as pd
import datetime

# Mengatur tampilan halaman web agar lebih lebar
st.set_page_config(page_title="Katalog Widget", layout="wide")

st.title("🎛️ Katalog Lengkap Fitur Interaktif Streamlit")
st.write("Coba mainkan semua tombol dan input di bawah ini!")

st.divider()

# Membagi layar menjadi dua kolom agar lebih rapi
kolom_kiri, kolom_kanan = st.columns(2)

with kolom_kiri:
    st.header("1. Pilihan Tunggal & Ganda")
    
    # 1. Checkbox (Kotak Centang)
    st.subheader("Checkbox")
    setuju = st.checkbox("Saya setuju dengan syarat dan ketentuan")
    if setuju:
        st.success("Bagus! Kamu sudah mencentang kotaknya.")

    # 2. Radio Button (Pilihan Tunggal)
    st.subheader("Radio Button")
    gender = st.radio("Pilih jenis kelamin:", ["Laki-laki", "Perempuan", "Rahasia"])
    st.info(f"Pilihanmu: {gender}")

    # 3. Selectbox (Dropdown Pilihan Tunggal)
    st.subheader("Selectbox (Dropdown)")
    kota = st.selectbox("Pilih asal kota:", ["Jakarta", "Bandung", "Surabaya", "Yogyakarta"])
    st.info(f"Kamu memilih kota: {kota}")

    # 4. Multiselect (Dropdown Pilihan Ganda)
    st.subheader("Multiselect")
    hobi = st.multiselect("Pilih hobi (bisa lebih dari satu):", ["Membaca", "Main Game", "Olahraga", "Coding"])
    st.info(f"Hobi yang dipilih: {hobi}")


with kolom_kanan:
    st.header("2. Input Angka & Waktu")
    
    # 5. Slider (Penggeser Angka Tunggal)
    st.subheader("Slider Tunggal")
    umur = st.slider("Berapa umurmu?", min_value=0, max_value=100, value=20)
    st.info(f"Umurmu: {umur} tahun")

    # 6. Slider Rentang (Memilih Jarak Angka)
    st.subheader("Slider Rentang")
    rentang_harga = st.slider("Pilih rentang harga:", min_value=0, max_value=1000, value=(200, 500))
    st.info(f"Harga dari {rentang_harga[0]} sampai {rentang_harga[1]}")

    # 7. Number Input (Ketik Angka)
    st.subheader("Number Input")
    berat = st.number_input("Masukkan berat badan (kg):", min_value=0.0, value=60.0, step=0.5)
    st.info(f"Berat badan: {berat} kg")

    # 8. Date Input (Pilih Tanggal)
    st.subheader("Date Input")
    tanggal = st.date_input("Kapan kamu ulang tahun?", datetime.date(2000, 1, 1))
    st.info(f"Tanggal lahir: {tanggal}")

st.divider()

st.header("3. Input Teks & Tombol Aksi")

# 9. Text Input (Teks Pendek)
nama = st.text_input("Ketik nama lengkapmu di sini:")
if nama:
    st.write(f"Halo, **{nama}**! Selamat datang di dashboard.")

# 10. Text Area (Teks Panjang)
komentar = st.text_area("Tuliskan masukan atau ulasanmu:")
if komentar:
    st.write(f"Komentarmu: *{komentar}*")

# 11. File Uploader (Unggah File - Sangat berguna untuk data csv)
st.subheader("File Uploader")
file_unggahan = st.file_uploader("Coba unggah file CSV atau Excel di sini", type=['csv', 'xlsx'])
if file_unggahan is not None:
    st.success("File berhasil diunggah! (Ini hanya simulasi)")

# 12. Button (Tombol Klik)
st.subheader("Tombol Aksi (Button)")
st.write("Klik tombol di bawah ini untuk melihat efeknya:")
if st.button("🚀 Luncurkan Roket!"):
    st.balloons() # Ini fitur rahasia Streamlit untuk memunculkan balon animasi!
    st.success("Wussss! Roket berhasil diluncurkan!")

# --- BONUS: Menaruh fitur di Sidebar ---
st.sidebar.header("Panel Samping (Sidebar)")
st.sidebar.write("Kamu juga bisa menaruh semua fitur interaktif tadi di sini agar halaman utama tidak penuh.")
tema_gelap = st.sidebar.checkbox("Aktifkan Tema Gelap (Hanya teks)")
if tema_gelap:
    st.sidebar.write("Teks tema gelap aktif!")
