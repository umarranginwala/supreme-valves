import pypdf
import json

def extract_text_from_pdf(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n\n--- PAGE BREAK ---\n\n"
    return text

if __name__ == "__main__":
    pdf_path = "/Users/umarranginwala/Downloads/supremevalves_site_v3/catalogue/BOSS.pdf"
    text = extract_text_from_pdf(pdf_path)
    with open("boss_content.txt", "w") as f:
        f.write(text)
    print("Extracted text to boss_content.txt")
