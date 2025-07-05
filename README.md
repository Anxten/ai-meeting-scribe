# 🤖 AI Notulis Rapat Otonom

Sebuah aplikasi Python yang mampu "mendengarkan" rekaman audio rapat dan secara otomatis membuat notulensi yang terstruktur, lengkap dengan ringkasan, keputusan kunci, dan daftar *action items*.

---

## 🎯 Masalah yang Dipecahkan

Setiap organisasi menghabiskan waktu berjam-jam setiap minggunya untuk membuat notulensi rapat. Proyek ini bertujuan untuk mengotomatiskan proses tersebut, mengubah file audio berdurasi panjang menjadi laporan strategis dalam hitungan menit, menghemat waktu dan meningkatkan produktivitas.

---

## ⚙️ Arsitektur Solusi

Aplikasi ini bekerja dalam dua tahap utama:

1.  **Fase Transkripsi (Speech-to-Text):** Menggunakan model **Whisper (dari OpenAI)** yang dijalankan secara lokal untuk mengubah file audio menjadi transkrip teks mentah dengan akurasi tinggi. Menjalankan model secara lokal menjamin privasi data.
2.  **Fase Analisis & Ekstraksi:** Transkrip mentah tersebut kemudian dianalisis oleh sebuah *chain* **LangChain** yang ditenagai oleh **LLM Groq (model Llama 3)**. AI diberi prompt untuk bertindak sebagai notulis profesional dan mengekstrak informasi terstruktur.

---

## 💻 Tumpukan Teknologi (Tech Stack)

* **Python**
* **Whisper (OpenAI)**: Untuk transkripsi Audio-ke-Teks secara lokal.
* **LangChain**: Sebagai framework utama untuk orkestrasi dan interaksi dengan LLM.
* **Groq API (Llama 3)**: Berperan sebagai "otak" atau LLM yang melakukan analisis teks.
* **ffmpeg**: Sebagai prasyarat sistem untuk pemrosesan audio oleh Whisper.

---

## 🚀 Instalasi & Setup

### Prasyarat
Pastikan **`ffmpeg`** sudah terinstall di sistem Anda. (Panduan untuk Windows: `https://www.gyan.dev/ffmpeg/builds/`).

### Langkah-langkah
1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/Anxten/ai-meeting-scribe.git](https://github.com/Anxten/ai-meeting-scribe.git)
    cd ai-meeting-scribe
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install semua library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Buat file `.env` dan masukkan kunci API Groq Anda:**
    ```
    GROQ_API_KEY='gsk_...'
    ```

---

## ▶️ Cara Penggunaan

1.  Letakkan file audio Anda (misalnya `pidato_jokowi.mp3`) di dalam folder utama proyek.
2.  Buka file `app.py` dan ubah nama file di dalam variabel `audio_file_path`.
3.  Jalankan aplikasi dari terminal:
    ```bash
    python app.py
    ```

---

## ✨ Contoh Hasil

**NOTULENSI RAPAT:**

Berikut adalah notulensi yang jelas dan terstruktur berdasarkan transkrip mentah yang diberikan:

1. Ringkasan Rapat:
Rapat ini membahas tentang pentingnya memanfaatkan peluang besar yang dimiliki Indonesia untuk menjadi salah satu dari 5 besar ekonomi dunia pada tahun 2045...

2. Keputusan Kunci yang Dibuat:

Mempersiapkan sumber daya manusia dan sektor ekonomi hijau untuk mencapai tujuan menjadi negara maju.

Melakukan hilirisasi untuk mengolah sumber daya alam dan memberikan nilai tambah.

3. Action Items (Tugas & Penanggung Jawab):

Mempersiapkan anggaran perlindungan sosial total...

Melakukan upscaling tenaga kerja melalui balai latihan kerja...