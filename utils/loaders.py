from langchain_community.document_loaders import (
    PyMuPDFLoader,
    Docx2txtLoader,
    UnstructuredPowerPointLoader,
    TextLoader,
)
from langchain_core.documents import Document
import pandas as pd
import os


def load_document(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return PyMuPDFLoader(file_path).load()
    elif ext == ".docx":
        return Docx2txtLoader(file_path).load()
    elif ext == ".pptx":
        return UnstructuredPowerPointLoader(file_path).load()
    elif ext == ".csv":
        df = pd.read_csv(file_path)
        text = df.to_string(index=False)
        return [Document(page_content=text)]
    elif ext in [".txt", ".md"]:
        return TextLoader(file_path).load()
    else:
        raise ValueError(f"Unsupported file type: {ext}")
