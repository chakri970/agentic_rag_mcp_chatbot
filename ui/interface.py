import streamlit as st
from uuid import uuid4
import os
from mcp.message import MCPMessage


class UI:
    def __init__(self, bus):
        self.bus = bus
        self.trace_id = None
        self.answer = None
        self.sources = []
        self._register_ui_handler()

    def _register_ui_handler(self):
        def handle_response(msg):
            if msg.type == "FINAL_ANSWER" and msg.trace_id == self.trace_id:
                self.answer = msg.payload.get("answer", "No answer received.")
                self.sources = msg.payload.get("sources", [])
        self.bus.register_agent("UI", handle_response)

    def run(self):
        st.set_page_config(page_title="Agentic RAG Chatbot", layout="centered")
        st.title("📄 Agentic RAG Chatbot with MCP")

        uploaded_file = st.file_uploader(
            "📤 Upload a document",
            type=["pdf", "pptx", "csv", "docx", "txt", "md"]
        )        
        if uploaded_file:
            save_path = os.path.join("uploads", uploaded_file.name)
            os.makedirs("uploads", exist_ok=True)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            self.trace_id = str(uuid4())
            self.answer = None
            self.sources = []

            # Send correct DOCUMENT_UPLOAD message with list of documents
            upload_msg = MCPMessage(
                sender="UI",
                receiver="IngestionAgent",
                type="DOCUMENT_UPLOAD",           # Correct message type
                trace_id=self.trace_id,
                payload={"documents": [save_path]}  # List of files expected
            )
            self.bus.send(upload_msg)
            st.success(
                f" Uploaded {uploaded_file.name} and sent for processing.")

        query = st.text_input("🔍 Ask a question about the uploaded document:")
        if st.button("Ask"):
            if not self.trace_id:
                st.warning(
                    "Please upload a document before asking a question.")
            elif not query.strip():
                st.warning("Please enter a valid query.")
            else:
                query_msg = MCPMessage(
                    sender="UI",
                    receiver="RetrievalAgent",
                    type="QUERY",
                    trace_id=self.trace_id,
                    payload={"query": query}
                )
                self.bus.send(query_msg)
                st.info("Query sent. Waiting for response...")

        if self.answer:
            st.markdown("---")
            st.subheader("Answer")
            st.write(self.answer)

            if self.sources:
                st.subheader(" Sources")
                for src in self.sources:
                    st.markdown(f"- {src}")
