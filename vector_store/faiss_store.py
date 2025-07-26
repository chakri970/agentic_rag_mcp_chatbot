from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List, Optional
import os


class VectorStore:
    def __init__(self, embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize the FAISS vector store with HuggingFace embeddings.
        Creates an empty index on init.
        """
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

        # Create an initial FAISS index with a dummy document to initialize the index
        init_doc = Document(page_content="Init", metadata={"doc_id": "Init"})
        self.store = FAISS.from_documents([init_doc], self.embeddings)

        # Remove the dummy document immediately
        existing_ids = list(self.store.index_to_docstore_id.values())
        if "Init" in existing_ids:
            try:
                self.store.delete(["Init"])
            except Exception:
                pass  # Ignore if it does not exist

    def add_documents(self, documents: List[Document]) -> None:
        """
        Add documents to the FAISS store.
        """
        self.store.add_documents(documents)

    def similarity_search(self, query: str, k: int = 5) -> List[Document]:
        """
        Search the vector store and return top-k similar documents.
        """
        return self.store.similarity_search(query, k=k)

    def query(self, query: str, k: int = 5) -> List[Document]:
        """
        Alias for similarity_search to keep API consistent.
        """
        return self.similarity_search(query, k)

    def delete(self, ids: List[str]) -> None:
        """
        Delete documents by their IDs.
        """
        try:
            self.store.delete(ids)
        except Exception:
            # If IDs not found or deletion fails, ignore or log here
            pass

    def save(self, folder_path: str) -> None:
        """
        Save FAISS index and embeddings locally.
        """
        os.makedirs(folder_path, exist_ok=True)
        self.store.save_local(folder_path=folder_path)

    @classmethod
    def load(cls, folder_path: str, embedding_model: Optional[str] = None) -> "VectorStore":
        """
        Load a FAISS index from local storage.
        """
        embedding_model = embedding_model or "sentence-transformers/all-MiniLM-L6-v2"
        embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

        instance = cls.__new__(cls)
        instance.embeddings = embeddings
        instance.store = FAISS.load_local(folder_path=folder_path, embeddings=embeddings)
        return instance
