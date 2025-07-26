from langchain_community.document_loaders import PyMuPDFLoader, Docx2txtLoader, UnstructuredPowerPointLoader, CSVLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List


def load_document(file_path: str):
    """
    Load documents from various file formats.

    Supported: PDF, DOCX, PPTX, CSV, TXT/Markdown
    """
    if file_path.endswith(".pdf"):
        loader = PyMuPDFLoader(file_path)
    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
    elif file_path.endswith(".pptx"):
        loader = UnstructuredPowerPointLoader(file_path)
    elif file_path.endswith(".csv"):
        loader = CSVLoader(file_path)
    elif file_path.endswith(".txt") or file_path.endswith(".md"):
        loader = TextLoader(file_path, encoding="utf-8")
    else:
        raise ValueError(
            "Unsupported file type. Supported types: pdf, docx, pptx, csv, txt, md")

    return loader.load()


def parse_documents(file_paths: List[str], chunk_size: int = 500, chunk_overlap: int = 100):
    """
    Load and split multiple documents into chunks for downstream processing.

    Args:
        file_paths: List of document file paths.
        chunk_size: Max characters per chunk.
        chunk_overlap: Overlap between chunks to preserve context.

    Returns:
        List of langchain.schema.Document chunks.
    """
    all_chunks = []
    for path in file_paths:
        documents = load_document(path)
        print(f"[Parser] Loaded {len(documents)} documents from {path}")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = splitter.split_documents(documents)

        # Filter out empty chunks
        chunks = [chunk for chunk in chunks if chunk.page_content.strip()]
        print(f"[Parser] After filtering, {len(chunks)} non-empty chunks")

        # Show sample chunk previews
        for i, chunk in enumerate(chunks[:3]):
            print(
                f"[Parser] Sample chunk {i+1} preview:\n{chunk.page_content[:200]}...\n")

        all_chunks.extend(chunks)

    print(f"[Parser] Total chunks parsed: {len(all_chunks)}")
    return all_chunks
