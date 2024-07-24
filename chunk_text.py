import os

def chunk_text(text, chunk_size=1000):
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

if __name__ == "__main__":
    for i in range(1, 4):
        with open(f"E:/TEXT_EXTRACTION_LLM/data/textbook{i}.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            chunks = chunk_text(text)
            with open(f"E:/TEXT_EXTRACTION_LLM/data/chunks_textbook{i}.txt", 'w', encoding='utf-8') as chunk_file:
                for chunk in chunks:
                    chunk_file.write(chunk + "\n")
