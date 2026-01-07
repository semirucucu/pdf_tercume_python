# PDF Translator (EN → TR)

Python ile PDF dosyalarını İngilizce'den Türkçe'ye çeviren bir proje.

## Özellikler
- PDF metin çıkarma (PyMuPDF)
- Otomatik çeviri (Google Translate)
- Unicode destekli PDF oluşturma
- Türkçe karakter sorunu yok

## Kurulum
```bash
pip install pymupdf deep-translator reportlab

## Kullanım
main.py dosyasında input_pdf dosya yolunu ve output_pdf dosya adını kendi pdf dosyanıza göre değiştirin ve main.py yi çalıştırın
