# app.py

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Impor fungsi yang baru saja kita buat
from transcriber import transcribe_audio

# Setup dasar
load_dotenv()
llm = ChatGroq(model_name="llama3-70b-8192", temperature=0, api_key=os.getenv("GROQ_API_KEY"))

# Nama file audio yang akan dianalisis
audio_file_path = "pidato_jokowi.mp3"

# --- LANGKAH 1: UBAH AUDIO MENJADI TEKS ---
print(f"--- [LANGKAH 1] Memproses audio dari '{audio_file_path}'... ---")
transkrip_rapat = transcribe_audio(audio_file_path)

if "ERROR" in transkrip_rapat:
    print(transkrip_rapat)
else:
    print("--- Transkrip berhasil dibuat. ---")
    
    # --- LANGKAH 2: ANALISIS TEKS DENGAN AI ---
    print("\n--- [LANGKAH 2] Mengirim transkrip ke AI untuk dibuat notulensi... ---")
    
    # Prompt engineering canggih untuk membuat notulensi terstruktur
    prompt = ChatPromptTemplate.from_template(
        "Anda adalah seorang Notulis Rapat Profesional yang sangat efisien.\n"
        "Tugas Anda adalah membaca transkrip rapat mentah berikut dan mengubahnya menjadi notulensi yang jelas dan terstruktur.\n\n"
        "TRANSKRIP MENTAH:\n"
        "-----------------\n"
        "{transkrip}\n"
        "-----------------\n\n"
        "Instruksi: Berdasarkan transkrip di atas, ekstrak informasi berikut dan sajikan dalam format di bawah ini. Jika sebuah bagian tidak ada, tulis 'Tidak ada'.\n\n"
        "**1. Ringkasan Rapat:**\n"
        "[Tulis satu paragraf ringkasan utama dari rapat di sini]\n\n"
        "**2. Keputusan Kunci yang Dibuat:**\n"
        "- [Tulis poin keputusan pertama]\n"
        "- [Tulis poin keputusan kedua]\n\n"
        "**3. Action Items (Tugas & Penanggung Jawab):**\n"
        "- [Tulis action item pertama, sebutkan siapa yang bertanggung jawab jika ada]\n"
        "- [Tulis action item kedua]"
    )

    # Membuat dan menjalankan rantai analisis
    rantai_notulen = prompt | llm | StrOutputParser()
    notulensi_final = rantai_notulen.invoke({"transkrip": transkrip_rapat})

    # Menampilkan hasil akhir
    print("\n\n==================== NOTULENSI RAPAT ====================")
    print(notulensi_final)
    print("=========================================================")