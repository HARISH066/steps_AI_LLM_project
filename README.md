# Textbook Content Extraction and Question-Answering System

## Overview

This project demonstrates the process of extracting content from digital textbooks, creating a vector database using Whoosh, and developing a question-answering system using an LLM (Language Model). The project leverages Streamlit to provide a user-friendly interface for interacting with the system.

## Features

1. **Content Extraction**: Extracts text content from uploaded PDF textbooks.
2. **Data Chunking**: Chunks the extracted content into short texts for indexing.
3. **Indexing with Whoosh**: Indexes the chunked texts using the Whoosh search engine.
4. **Query Expansion**: Expands user queries using synonyms for better search results.
5. **Question Answering**: Uses OpenAI GPT-3 to generate answers based on retrieved content.
6. **User Interface**: Provides an easy-to-use interface via Streamlit.

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.6 or higher
- pip (Python package installer)

### Dependencies

Install the necessary dependencies using the following command:

```bash
pip install streamlit PyPDF2 whoosh nltk openai
