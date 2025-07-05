# dashboard.py (Versi Final Terintegrasi)

import streamlit as st
import os
from transcriber import transcribe_audio # Impor fungsi transkripsi kita
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# --- KONFIGURASI DAN SETUP ---
# Setup halaman Streamlit
st.set_page_config(
    page_title="AI Notulis Rapat",
    page_icon="🤖",
    layout="wide"
)

# Memuat kunci API dari file .env
load_dotenv()

# Inisialisasi LLM sekali saja untuk efisiensi
# Kita letakkan di sini agar tidak dibuat ulang setiap kali tombol diklik
llm = ChatGroq(
    model_name="llama3-70b-8192", 
    temperature=0, 
    api_key=os.getenv("GROQ_API_KEY")
)

# Template prompt untuk analisis
analysis_prompt = ChatPromptTemplate.from_template(
    "Anda adalah seorang Notulis Rapat Profesional yang sangat efisien.\n"
    "Tugas Anda adalah membaca transkrip rapat mentah berikut dan mengubahnya menjadi notulensi yang jelas dan terstruktur.\n\n"
    "TRANSKRIP MENTAH:\n"
    "-----------------\n"
    "{transkrip}\n"
    "-----------------\n\n"
    "Instruksi: Berdasarkan transkrip di atas, ekstrak informasi berikut dan sajikan dalam format markdown yang rapi. Jika sebuah bagian tidak ada informasinya, tulis 'Tidak ada informasi yang relevan'.\n\n"
    "**1. Ringkasan Rapat:**\n"
    "- [Tulis satu paragraf ringkasan utama dari rapat di sini]\n\n"
    "**2. Keputusan Kunci yang Dibuat:**\n"
    "- [Tulis poin keputusan pertama]\n"
    "- [Tulis poin keputusan kedua]\n\n"
    "**3. Action Items (Tugas & Penanggung Jawab):**\n"
    "- [Tulis action item pertama, sebutkan siapa yang bertanggung jawab jika ada]\n"
    "- [Tulis action item kedua]"
)

# Membuat rantai analisis
analysis_chain = analysis_prompt | llm | StrOutputParser()

# --- TAMPILAN APLIKASI WEB ---
st.title("🤖 AI Notulis Rapat Otonom")
st.write("Unggah file audio rapat Anda (.mp3, .m4a, .wav), dan biarkan AI yang membuat notulensinya untuk Anda.")

uploaded_file = st.file_uploader(
    "Pilih sebuah file audio untuk dianalisis...",
    type=['mp3', 'm4a', 'wav']
)

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/wav')
    st.success(f"File '{uploaded_file.name}' berhasil diunggah.")

    if st.button("Mulai Analisis Sekarang 🚀"):
        # Tampilkan spinner saat proses backend berjalan
        with st.spinner('AI sedang bekerja... Proses ini bisa memakan waktu beberapa menit, mohon tunggu.'):
            
            # 1. Simpan file yang diunggah ke lokasi sementara
            temp_audio_path = os.path.join("temp_audio", uploaded_file.name)
            os.makedirs("temp_audio", exist_ok=True)
            with open(temp_audio_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # 2. Panggil fungsi transkripsi dari transcriber.py
            st.info("Tahap 1 dari 2: Mengubah audio menjadi teks (Transkripsi)...")
            transkrip_rapat = transcribe_audio(temp_audio_path)

            # 3. Panggil rantai analisis LangChain
            if "ERROR" not in transkrip_rapat:
                st.info("Tahap 2 dari 2: Menganalisis transkrip dan membuat notulensi...")
                notulensi_final = analysis_chain.invoke({"transkrip": transkrip_rapat})
                
                # 4. Tampilkan hasil akhir
                st.subheader("✅ Analisis Selesai! Berikut adalah hasilnya:")
                st.markdown(notulensi_final)
            else:
                st.error(f"Gagal melakukan transkripsi: {transkrip_rapat}")
            
            # Hapus file audio sementara setelah selesai
            os.remove(temp_audio_path)