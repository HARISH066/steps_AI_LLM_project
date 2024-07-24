# Textbook Content Extraction and Question-Answering System

## Overview

This project demonstrates the process of extracting content from digital textbooks, creating a vector database using Whoosh, and developing a question-answering system using an LLM (Language Model). The project leverages Streamlit to provide a user-friendly interface for interacting with the system.

## Selected Textbooks

The selected textbooks for content extraction, each with more than 300 pages, are:

1. **Title 1**: [https://lookingfortruth.org/wp-content/uploads/2018/04/Men-are-from-mars-women-are-from-venus.pdf](#)
2. **Title 2**: [https://pdfdrive.com.co/reality-transurfing-pdf-a/](#)
3. **Title 3**: [https://amzn.in/d/06sIfpOc](#)

## Project Components

1. **Content Extraction**:
   - Extracts text content from uploaded PDF textbooks.
   - Utilizes `PyPDF2` for extracting text from PDF files.

2. **Data Chunking**:
   - Chunks the extracted content into short, contiguous texts of approximately 100 tokens each, preserving sentence boundaries.
   - Uses `NLTK` for tokenization.

3. **RAPTOR Indexing**:
   - Implements clustering using Gaussian Mixture Models (GMMs) with soft clustering.
   - Summarizes clusters using GPT-3.5-turbo.
   - Re-embeds summarized texts and recursively applies the clustering and summarization process to form a hierarchical tree structure.

4. **Retrieval Techniques**:
   - Employs query expansion techniques and hybrid retrieval methods.
   - Combines BM25 and BERT-based retrieval methods.
   - Uses Whoosh for indexing and retrieval.

5. **Re-ranking Algorithms**:
   - Re-ranks retrieved data based on relevance and similarity to the query.

6. **Question Answering**:
   - Passes retrieved and re-ranked data to an LLM for generating accurate and relevant answers.

7. **User Interface**:
   - Developed using Streamlit.
   - Allows users to upload textbooks, input queries, and view retrieved answers along with textbook titles and page numbers.

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.6 or higher
- pip (Python package installer)

### Dependencies

Install the necessary dependencies using the following command:

```bash
pip install streamlit PyPDF2 whoosh nltk openai
