# Unified Retrieval-Augmented Multimodal Reasoning System
A modular multimodal RAG framework for grounded and explainable question answering over research documents.

## Overview
The **Unified Retrieval-Augmented Multimodal Reasoning System** is an AI framework designed to answer questions over **research documents containing both text and visual content**.

Unlike traditional RAG systems that operate only on text, this system integrates:
- text retrieval
- image/figure understanding
- cross-modal reasoning
- knowledge graph augmentation
- explainable answer generation

The system processes PDFs containing:
- paragraphs
- figures
- captions
- tables
- metadata

and produces **grounded answers supported by evidence**.

---

## Motivation
Research documents distribute information across multiple modalities:
- explanations in text
- results in tables
- insights in figures

Standard search and QA systems fail to connect these sources.

This project solves that by:
- retrieving multimodal evidence
- reasoning across modalities
- generating explainable answers

---

## Key Features

- PDF ingestion and parsing
- Text chunking and metadata extraction
- Figure and caption extraction
- Semantic text retrieval
- Multimodal retrieval (text + image)
- Cross-modal search using shared embeddings
- Retrieval-Augmented Generation (RAG)
- Evidence-grounded answer generation
- Knowledge graph construction and reasoning
- Explainable answer tracing
- Model evaluation and benchmarking

---

## System Architecture

The system consists of the following modules:

### 1. Ingestion
- Parse PDFs
- Extract text, images, captions, metadata

### 2. Embeddings
- Text embeddings using Sentence Transformers
- Image embeddings using CLIP

### 3. Retrieval
- Vector-based retrieval (FAISS / Chroma)
- Hybrid retrieval (text + image)
- Reranking

### 4. Reasoning
- Evidence fusion
- Prompt construction
- Answer generation

### 5. Knowledge Graph
- Entity extraction
- Relation extraction
- Graph construction
- Graph-based retrieval

### 6. Evaluation
- Retrieval quality metrics
- Answer accuracy
- Faithfulness
- Latency benchmarking

### 7. Application Layer
- Interactive demo using Streamlit

---

## Example Use Case

A user uploads a research paper and asks:

- "Which figure supports the performance claim?"
- "What does the paper say about model accuracy?"
- "Explain the relationship between CLIP and cross-modal retrieval."

The system:
1. retrieves relevant text and figures
2. links them via semantic similarity or graph relations
3. generates an answer
4. shows supporting evidence

---

## Research Adaptability

This project is designed as a **single modular system** that can be adapted for multiple research domains.

---

## Tech Stack

- Python
- Sentence Transformers
- CLIP (for multimodal embeddings)
- FAISS / ChromaDB
- PyMuPDF / pdfplumber
- spaCy / OpenIE
- NetworkX / Neo4j
- Streamlit

---

## Project Structure

src/
├── ingestion/
├── embeddings/
├── retrieval/
├── reasoning/
├── kg/
├── evaluation/
├── pipelines/
└── app/

---

## Installation

```bash
git clone https://github.com/yourusername/unified-mm-rag.git
cd unified-mm-rag

pip install -r requirements.txt

## Running the Project

Step 1: Ingest data
```bash
python scripts/ingest_data.py

Step 2: Create embeddings
```bash
python scripts/create_embeddings.py

Step 3: Build index
```bash
python scripts/build_vector_index.py

Step 4: Run RAG pipeline
```bash
python scripts/run_demo.py

Step 5: Launch app
```bash
streamlit run src/app/streamlit_app.py

---

## Evaluation
Evaluate the system using:
-Precision@k
-Recall@k
-MRR / nDCG
-Answer correctness
-Faithfulness
-Latency

---

## Future Work
-table-aware reasoning
-advanced multimodal reranking
-multi-hop reasoning
-improved KG reasoning

---

Author
Navya
