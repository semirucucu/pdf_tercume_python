import fitz  # PyMuPDF
from deep_translator import GoogleTranslator
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# -------------------------------
# PDF'DEN METİN OKUMA
# -------------------------------
def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    return full_text


# -------------------------------
# METNİ PARÇALAYARAK ÇEVİRME
# -------------------------------
def translate_text(text, source="en", target="tr", chunk_size=4000):
    translator = GoogleTranslator(source=source, target=target)
    translated_text = ""

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        translated_text += translator.translate(chunk) + "\n"

    return translated_text


# -------------------------------
# ÇEVRİLMİŞ METNİ PDF YAPMA
# -------------------------------
def text_to_pdf(text, output_pdf):
    pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))

    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    x_margin = 40
    y_margin = 40
    y_position = height - y_margin

    c.setFont("DejaVu", 10)

    wrapped_lines = wrap(text, 90)

    for line in wrapped_lines:
        if y_position <= y_margin:
            c.showPage()
            c.setFont("DejaVu", 10)
            y_position = height - y_margin

        c.drawString(x_margin, y_position, line)
        y_position -= 14

    c.save()


# -------------------------------
# ANA ÇALIŞMA
# -------------------------------
if __name__ == "__main__":
    input_pdf = "Bob Odenkirk - Comedy Comedy Comedy Drama.pdf"
    output_pdf = "Bob_Odenkirk_TR.pdf"

    print("📖 PDF okunuyor...")
    text = pdf_to_text(input_pdf)

    print("🌍 Çeviri yapılıyor (İngilizce → Türkçe)...")
    translated_text = translate_text(text)

    print("📝 Yeni PDF oluşturuluyor...")
    text_to_pdf(translated_text, output_pdf)

    print("✅ İşlem tamamlandı!")
    print(f"📄 Oluşturulan dosya: {output_pdf}")
