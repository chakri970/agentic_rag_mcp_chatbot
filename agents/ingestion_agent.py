from agents.base_agent import BaseAgent
from mcp.message import MCPMessage
from utils.parser_utils import parse_documents
from utils.loaders import load_document


class IngestionAgent(BaseAgent):
    def receive(self, message: MCPMessage):
        print(
                (
                    f"[IngestionAgent] Received message: {message.type} "
                    f"with payload keys {list(message.payload.keys())}"
                )
            )

        if message.type != "DOCUMENT_UPLOAD":
            return

        docs = message.payload["documents"]
        print(f"[IngestionAgent] Parsing {len(docs)} documents: {docs}")

        parsed_chunks = parse_documents(docs)
        print(f"[IngestionAgent] Parsed into {len(parsed_chunks)} chunks")

        response = MCPMessage(
            type="INGESTION_RESULT",
            sender=self.name,
            receiver="RetrievalAgent",
            trace_id=message.trace_id,
            payload={"chunks": parsed_chunks}
        )
        self.send(response)
