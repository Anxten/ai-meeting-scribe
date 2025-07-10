# 🤖 AI Notulis Rapat Otonom

Sebuah aplikasi Python yang mampu "mendengarkan" rekaman audio rapat dan secara otomatis membuat notulensi yang terstruktur, lengkap dengan ringkasan, daftar keputusan kunci, dan daftar *action items*.

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
* **Streamlit**: Untuk membangun antarmuka pengguna (UI) web yang interaktif.
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
5.  **Download File Audio Sampel:**
    * Download file audio sampel dari link Google Drive berikut dan letakkan di dalam folder proyek:
    * [Link Download Pidato Jokowi.mp3](https://drive.google.com/file/d/1syRPnhkVZ4DZ89SzxqXk5gA-xn2mNxzl/view?usp=sharing)


---

## ▶️ Cara Penggunaan

Aplikasi ini dijalankan sebagai aplikasi web interaktif.

1.  Pastikan file audio sampel (misalnya `pidato_jokowi.mp3`) sudah berada di dalam folder utama proyek.
2.  Jalankan aplikasi dari terminal:
    ```bash
    streamlit run dashboard.py
    ```
3.  Buka browser Anda, akses alamat `localhost` yang diberikan, unggah file audio, dan klik tombol "Mulai Analisis".

---

## ✨ Contoh Hasil

Berikut adalah contoh output saat menganalisis pidato kenegaraan:

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

> 💡 **Baca studi kasus lengkap** tentang bagaimana proyek ini dibangun di artikel LinkedIn saya: [Studi Kasus: Membangun AI Notulis Rapat dari Nol](https://www.linkedin.com/posts/allan-jeremy-bendatu-4425a3373_ai-python-langchain-activity-7349051782313979904-YwyA?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFx1LLIBCfsdlHy4v8cCaKNkYV997rwvbIo)