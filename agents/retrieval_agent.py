from agents.base_agent import BaseAgent
from mcp.message import MCPMessage
from vector_store.faiss_store import VectorStore


class RetrievalAgent(BaseAgent):
    def __init__(self, name, bus):
        super().__init__(name, bus)
        self.store = VectorStore()

    def receive(self, message: MCPMessage):
        print(f"[RetrievalAgent] Received message type: {message.type}")

        if message.type == "INGESTION_RESULT":
            chunks = message.payload.get("chunks", [])
            print(
                f"[RetrievalAgent] Adding {len(chunks)} chunks to "
                "vector store"
            )
            self.store.add_documents(chunks)

        elif message.type == "QUERY":
            query = message.payload.get("query", "")
            print(f"[RetrievalAgent] Processing query: {query}")

            top_chunks = self.store.query(query)
            print(
                f"[RetrievalAgent] Retrieved {len(top_chunks)} "
                "chunks from vector store"
            )

            filtered_chunks = [
                chunk for chunk in top_chunks
                if (
                    len(chunk.page_content.strip()) > 30
                    and chunk.page_content.strip().lower() != "init"
                )
            ]
            print(
                f"[RetrievalAgent] Filtered down to {len(filtered_chunks)} "
                "chunks after removing short or 'Init' chunks"
            )

            response = MCPMessage(
                type="RETRIEVAL_RESULT",
                sender=self.name,
                receiver="LLMResponseAgent",
                trace_id=message.trace_id,
                payload={
                    "retrieved_context": filtered_chunks,
                    "query": query
                }
            )
            print(
                "[RetrievalAgent] Sending RETRIEVAL_RESULT to "
                "LLMResponseAgent"
            )
            self.send(response)
