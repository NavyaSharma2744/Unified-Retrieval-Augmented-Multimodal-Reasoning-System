from setuptools import setup, find_packages

setup(
    name="unified_mm_rag",
    version="0.1.0",
    description="Unified Retrieval-Augmented Multimodal Reasoning System",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "sentence-transformers",
        "transformers",
        "torch",
        "faiss-cpu",
        "pymupdf",
        "pdfplumber",
        "Pillow",
        "opencv-python",
        "spacy",
        "networkx",
        "streamlit",
        "pyyaml",
        "loguru"
    ],
    python_requires=">=3.9",
)
