import streamlit as st
import PyPDF2
import os
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from whoosh import scoring
import nltk
from nltk.corpus import wordnet
import openai

# Initialize OpenAI API key
openai.api_key = "your_openai_api_key"

# Download necessary NLTK data
nltk.download('wordnet')

# Define the schema for the Whoosh index
schema = Schema(title=ID(stored=True), content=TEXT(stored=True))

# Create the index directory
index_dir = "indexdir"
if not os.path.exists(index_dir):
    os.mkdir(index_dir)

# Function to read PDF content
def read_pdf(pdf_path):
    for i in range(1, 4):
        pdf_path = f"E:/TEXT_EXTRACTION_LLM/data/textbook{i}.txt"
    content = ""
    reader = PyPDF2.PdfFileReader(pdf_path)
    for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            content += page.extractText()
            return content

# Function to chunk text
def chunk_text(text, chunk_size=100):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# Function to expand query
def expand_query(query_str):
    synonyms = set()
    for syn in wordnet.synsets(query_str):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return ' '.join(synonyms)

# Function to get answer from LLM
def get_answer_from_llm(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Textbook Content Extraction and QA System")

# File upload
uploaded_file = st.file_uploader("Upload a textbook (PDF)", type="pdf")

if uploaded_file is not None:
    # Extract and chunk content
    text_content = read_pdf(uploaded_file)
    chunks = chunk_text(text_content)
    
    # Create or open the Whoosh index
    if not index.exists_in(index_dir):
        ix = index.create_in(index_dir, schema)
    else:
        ix = index.open_dir(index_dir)

    # Add documents to the index
    writer = ix.writer()
    for i, chunk in enumerate(chunks):
        writer.add_document(title=f"textbook_chunk_{i+1}", content=chunk)
    writer.commit()
    
    st.write("Textbook content indexed successfully!")

    # Query input
    query_str = st.text_input("Enter your query:")
    if query_str:
        # Expand query
        expanded_query = expand_query(query_str)
        
        # Define the query parser
        qp = QueryParser("content", schema=ix.schema)
        
        # Parse the query
        query = qp.parse(expanded_query)
        
        # Use BM25 scoring
        searcher = ix.searcher(weighting=scoring.BM25F())
        
        # Perform the search
        results = searcher.search(query, limit=10)
        
        # Display results
        st.write("Top 10 relevant chunks:")
        context = ""
        for result in results:
            st.write(result['title'], result['content'])
            context += result['content'] + " "
        
        # Generate answer from LLM
        if context:
            question = st.text_input("Ask a question based on the retrieved content:")
            if question:
                prompt = f"Based on the following text, answer the question:\n\n{context}\n\nQuestion: {question}"
                answer = get_answer_from_llm(prompt)
                st.write("Answer:", answer)
