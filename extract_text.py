import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        number_of_pages = len(reader.pages)
        for page_num in range(number_of_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

if __name__ == "__main__":
    for i in range(1, 4):
        pdf_path = f"E:/TEXT_EXTRACTION_LLM/data/textbook{i}.pdf"
        text = extract_text_from_pdf(pdf_path)
        with open(f"E:/TEXT_EXTRACTION_LLM/data/textbook{i}.txt", 'w', encoding='utf-8') as text_file:
            text_file.write(text)
for i in range(1, 4):
    with open(f"../data/textbook{i}.txt", 'r', encoding='utf-8') as text_file:
        text = text_file.read()
        print(f"Contents of textbook{i}.txt:\n{text[:500]}\n{'-'*40}\n")