from agents.base_agent import BaseAgent
from mcp.message import MCPMessage
from utils.llm_utils import GPT4AllWrapper
from langchain.schema import Document


class LLMResponseAgent(BaseAgent):
    def __init__(self, name: str, bus):
        super().__init__(name, bus)
        self.llm = GPT4AllWrapper()  # CPU version

    def receive(self, message: MCPMessage):
        if message.type != "RETRIEVAL_RESULT":
            print(
                f"[LLMResponseAgent] Ignored message of type: {message.type}")
            return

        context = message.payload.get("retrieved_context", [])
        query = message.payload.get("query", "")

        print(f"[LLMResponseAgent] Received query: {query}")
        print(f"[LLMResponseAgent] Context chunks count: {len(context)}")

        for i, chunk in enumerate(context):
            print(f"Chunk {i + 1} preview: {chunk.page_content[:100]}")

        if not all(isinstance(c, Document) for c in context):
            print(
                "[LLMResponseAgent] Error: Context chunks must be of type "
                "langchain.schema.Document"
            )
            return

        answer = self.llm.query_llm(context, query)
        print(f"[LLMResponseAgent] Generated answer: {answer}")

        response = MCPMessage(
            type="FINAL_ANSWER",
            sender=self.name,
            receiver="UI",
            trace_id=message.trace_id,
            payload={
                "answer": answer,
                "sources": context
            }
        )

        self.send(response)
