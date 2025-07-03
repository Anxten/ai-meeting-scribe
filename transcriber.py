# transcriber.py

import whisper

def transcribe_audio(file_path: str):
    """
    Fungsi ini menerima path ke sebuah file audio, melakukan transkripsi
    menggunakan model Whisper 'base', dan mengembalikan teksnya.
    """
    print("Memuat model Whisper 'base'...")
    try:
        model = whisper.load_model("base")
        print("Model berhasil dimuat.")

        print(f"Memulai transkripsi file: {file_path}...")
        result = model.transcribe(file_path)

        print("Transkripsi berhasil.")
        return result["text"]
    except FileNotFoundError:
        return f"ERROR: File tidak ditemukan di path: {file_path}"
    except Exception as e:
        return f"ERROR: Terjadi error saat transkripsi: {e}"