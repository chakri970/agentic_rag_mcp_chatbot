from llama_cpp import Llama
from typing import List
from langchain.schema import Document
import os


class GPT4AllWrapper:
    def __init__(
        self,
        model_path: str = (
            "D:/agentic_rag_mcp_chatbot/llama_models/"
            "phi-2.Q4_K_M.gguf"
        ),
    ):
        if not os.path.isfile(model_path):
            raise FileNotFoundError(
                f"Model file does not exist at: {model_path}")

        print("[LLM] Loading model on CPU from:", model_path)

        # Load on CPU (no GPU layers set)
        self.model = Llama(
            model_path=model_path,
            n_ctx=1024,
            n_threads=os.cpu_count()
        )

        print("[LLM] Model loaded on CPU.")

    def query_llm(self, context_chunks: List[Document], question: str) -> str:
        filtered_chunks = [
            chunk.page_content.strip()
            for chunk in context_chunks
            if chunk.page_content.strip()
        ]
        if not filtered_chunks:
            return "No relevant context found to answer the question."

        max_context_length = 2000
        context = ""
        for chunk in filtered_chunks:
            if len(context) + len(chunk) > max_context_length:
                break
            context += chunk + "\n"

        prompt = (
            "You are a helpful assistant. Use the following context to answer "
            "the question.\n\n"
            f"Context:\n{context.strip()}\n\n"
            f"Question: {question}\n\nAnswer:"
        )

        output = self.model(
            prompt=prompt,
            max_tokens=64,
            temperature=0.4,
            top_p=0.9,
            stop=["\n\n", "Question:", "Context:"]
        )

        answer = output["choices"][0]["text"].strip()
        if not answer or "i don't know" in answer.lower():
            return (
                "The assistant could not confidently answer the question "
                "based on the given context."
            )

        return answer
