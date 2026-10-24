import streamlit as st
import pandas as pd

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Sistem Ringkasan Keluhan KRL iE305",
    page_icon="🚆",
    layout="wide"
)

# Judul Utama Web
st.title("🚆 Dasbor Ekstraksi Ringkasan Keluhan KRL Commuter Line Seri iE305")
st.markdown("---")

# Sidebar Pilihan Metode
st.sidebar.header("Navigasi Analisis")
menu = st.sidebar.radio(
    "Pilih Metode Peringkasan:", 
    ["Beranda / Ringkasan", "Metode TextRank", "Metode LSA"]
)

if menu == "Beranda / Ringkasan":
    st.header("Selamat Datang di Portal Evaluasi Ringkasan KRL iE305")
    st.write("""
        Aplikasi web ini menyajikan hasil ekstraksi ringkasan teks otomatis (*extractive text summarization*)
        dari ulasan dan keluhan pengguna KRL Commuter Line seri **iE305 (CLI-225 / CLI-226)** di media sosial X.
        
        Penelitian ini membandingkan dua pendekatan algoritma *unsupervised learning*:
        1. **TextRank:** Berbasis pemodelan jaringan graf (*graph-based*) dan pembobotan PageRank.
        2. **Latent Semantic Analysis (LSA):** Berbasis reduksi dimensi ruang topik (*TruncatedSVD*).
    """)
    st.info("👈 Silakan pilih metode pada menu navigasi di sebelah kiri untuk melihat detail hasil ringkasan dan evaluasinya.")

elif menu == "Metode TextRank":
    st.header("📄 Hasil Peringkasan Teks - Algoritma TextRank")
    st.write("Menampilkan *Top-10* kalimat ringkasan keluhan utama berdasarkan perankingan keterhubungan graf.")
    
    # Menampilkan Tabel CSV TextRank
    try:
        df_tr = pd.read_csv("skripsi_textrank_lsa/hasil_textrank.csv")
        st.subheader("Tabel Top-10 Ringkasan Kalimat (TextRank)")
        st.dataframe(df_tr, use_container_width=True)
    except Exception as e:
        st.error("File 'hasil_textrank.csv' belum ditemukan di GitHub.")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Visualisasi Jaringan Graf (NetworkX)")
        try:
            st.image("skripsi_textrank_lsa/visualisasi_graph_textrank.png", caption="Topologi Graf TextRank (Ambang Batas > 0.4)", use_container_width=True)
        except:
            st.warning("Gambar visualisasi graf belum diunggah.")
            
    with col2:
        st.subheader("Evaluasi Confusion Matrix (TextRank)")
        try:
            st.image("skripsi_textrank_lsa/confusion_matrix_textrank.png", caption="Confusion Matrix TextRank (Human Evaluation)", use_container_width=True)
        except:
            st.warning("Gambar Confusion Matrix belum diunggah.")

    st.markdown("---")
    st.subheader("Distribusi Skor Peringkat TextRank")
    try:
        st.image("skripsi_textrank_lsa/grafik_batang_top_textrank.png", caption="Distribusi Skor Top-10 Kalimat TextRank", use_container_width=True)
    except:
        st.warning("Gambar grafik batang TextRank belum diunggah.")

    st.markdown("---")
    st.subheader("📈 Metrik Evaluasi Kinerja (TextRank vs Human Expert)")
    
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Precision", value="100.00%")
    m2.metric(label="Recall", value="70.00%")
    m3.metric(label="F1-Score", value="82.35%")

elif menu == "Metode LSA":
    st.header("📊 Hasil Peringkasan Teks - Algoritma LSA (Latent Semantic Analysis)")
    st.write("Menampilkan *Top-10* kalimat ringkasan keluhan utama berdasarkan reduksi matriks konsep tersembunyi (*TruncatedSVD*).")
    
    # Menampilkan Tabel CSV LSA
    try:
        df_lsa = pd.read_csv("skripsi_textrank_lsa/hasil_lsa.csv")
        st.subheader("Tabel Top-10 Ringkasan Kalimat (LSA)")
        st.dataframe(df_lsa, use_container_width=True)
    except Exception as e:
        st.error("File 'hasil_lsa.csv' belum ditemukan di GitHub.")
        
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribusi Skor Signifikansi (L2-Norm)")
        try:
            st.image("skripsi_textrank_lsa/grafik_batang_top_lsa.png", caption="Grafik Batang Skor LSA", use_container_width=True)
        except:
            st.warning("Gambar grafik LSA belum diunggah.")
            
    with col2:
        st.subheader("Evaluasi Confusion Matrix (LSA)")
        try:
            st.image("skripsi_textrank_lsa/confusion_matrix_lsa.png", caption="Confusion Matrix LSA (Human Evaluation)", use_container_width=True)
        except:
            st.warning("Gambar Confusion Matrix belum diunggah.")

    st.markdown("---")
    st.subheader("📈 Metrik Evaluasi Kinerja (LSA vs Human Expert)")
    
    l1, l2, l3 = st.columns(3)
    l1.metric(label="Precision", value="60.00%")
    l2.metric(label="Recall", value="100.00%")
    l3.metric(label="F1-Score", value="75.00%")
