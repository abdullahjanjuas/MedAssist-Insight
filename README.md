# MedAssist-Insight
# MedAssist Insights – Generative & Agentic AI Medical Assistant

[Live Demo](link) | [Project Report / Paper](link)


## Overview

**MedAssist Insights** is an end-to-end **Generative and Agentic AI healthcare assistant** designed to process medical lab reports (PDFs) and generate structured, actionable insights. The system integrates **OCR, NLP, vector-based retrieval (RAG), and LLM-powered automation** to provide non-diagnostic explanations, highlight abnormal lab values, and suggest follow-up recommendations for healthcare professionals.

This project demonstrates a full-stack AI pipeline from raw data ingestion to interactive user-facing deployment.

---

## Features

- **PDF Ingestion & OCR:** Converts lab reports into structured text for analysis.  
- **ETL & Preprocessing:** Cleans, normalizes, and validates lab values; handles missing data and inconsistencies.  
- **RAG-based Knowledge Retrieval:** Integrates trusted medical references into a vector database for context-aware AI reasoning.  
- **Generative AI Automation:** Uses LLMs to generate non-diagnostic insights, abnormal value highlights, and structured recommendations.  
- **Interactive Streamlit Interface:** Allows users to upload lab reports, query insights, and visualize data interactively.  
- **Scalable & Optimized Pipeline:** Supports large document volumes, low-latency inference, and multi-user interactions.  

---

## Technology Stack

- **Programming Languages:** Python  
- **Data Processing & Analysis:** Pandas, NumPy, LLM-based structuring
- **Machine Learning / NLP:** PyTorch, embeddings, UMAP, 
- **Generative AI / LLM:** LangChain, HuggingFace models, LLM-based automation  
- **Vector Database / RAG:** chroma db, vector embeddings  
- **UI / Deployment:** Streamlit  
- **Other Tools:** OCR (PyTesseract), PDF parsing libraries

---

## Project Pipeline

1. **Data Ingestion:** Upload PDF lab reports.  
2. **Text Extraction:** Convert PDFs to text using OCR.  
3. **Preprocessing & Normalization:** Clean data, normalize lab values, handle missing/inconsistent data.  
4. **Vector Embedding & RAG:** Embed medical knowledge base and query using vector search.  
5. **LLM-based Generative Insights:** Generate non-diagnostic insights, detect abnormal results, provide structured recommendations.  
6. **Interactive Visualization:** Streamlit app allows querying, exploring, and downloading structured results.  

---

## Installation

```bash
# Clone the repository
git clone https://github.com/abdullahjanjuas/MedAssist-Insights.git
cd MedAssist-Insights

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
