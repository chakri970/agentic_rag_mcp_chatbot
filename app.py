# app.py

from mcp.bus import MCPBus
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent
from ui.interface import UI


def main():
    # Initialize the message bus
    bus = MCPBus()

    # Register all agents with the bus
    IngestionAgent("IngestionAgent", bus)
    RetrievalAgent("RetrievalAgent", bus)
    LLMResponseAgent("LLMResponseAgent", bus)

    # Launch the Streamlit UI
    ui = UI(bus)
    ui.run()


if __name__ == "__main__":
    main()
