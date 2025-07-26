#  Agentic RAG Chatbot for Multi-Format Document QA using Model Context Protocol (MCP)

## Project Overview

This project implements an **Agentic Retrieval-Augmented Generation (RAG) Chatbot** capable of answering user queries based on uploaded documents of various formats.  
The chatbot is designed with modular agents communicating through a **Model Context Protocol (MCP)**, ensuring scalable and maintainable architecture.

---

## Features

- **Multi-format Document Support:** Upload & process PDF, PPTX, DOCX, CSV, TXT/Markdown files.
- **Agent-based Modular Architecture:**  
  - `IngestionAgent` — parses and preprocesses documents.  
  - `RetrievalAgent` — embeds and retrieves relevant document chunks using FAISS vector store.  
  - `LLMResponseAgent` — generates answers by querying Large Language Models with retrieved context.
- **Model Context Protocol (MCP):** Agents communicate via structured JSON messages, enabling clear message passing and coordination.
- **Interactive Streamlit UI:**  
  - Upload multiple documents  
  - Multi-turn conversational interface  
  - View answers with source context links

---

## Tech Stack

- **Language:** Python 3.11
- **Agents & Messaging:** Custom MCP protocol, modular agent classes
- **Vector Database:** FAISS
- **Embeddings:** sentence-transformers
- **LLM:** phi-2.Q4_K_M.gguf quantized model via llama.cpp
- **UI Framework:** Streamlit
- **Document Parsing:** PyMuPDF (PDF), python-pptx, python-docx, pandas (CSV), markdown

---

##  Model Used

- **LLM**: [Phi-2.Q4_K_M](https://huggingface.co/TheBloke/phi-2-GGUF/blob/main/phi-2.Q4_K_M.gguf)  
  - Open-weight transformer model fine-tuned for instruction following and reasoning
- **Embeddings**: `sentence-transformers` 
- **Vector Database**: FAISS

---
---

##  Supported File Types

-  PDF (`.pdf`)
-  Word Document (`.docx`)
-  PowerPoint (`.pptx`)
-  CSV (`.csv`)
-  Plain/Text Markdown (`.txt`, `.md`)

---

### Clone the Repository

```bash
git clone https://github.com/chakri970/agentic_rag_mcp_chatbot.git
cd agentic_rag_mcp_chatbot
```

### Install Dependencies
```bash
pip install -r requirements.txt
```
### Download and place model file

Download the quantized phi-2 model (TheBloke/phi-2.Q4_K_M.gguf) and place it inside the models/ directory.
https://huggingface.co/TheBloke/phi-2-GGUF/blob/main/phi-2.Q4_K_M.gguf

### Run the Application
```bash
streamlit run main.py
```

## What is Model Context Protocol (MCP)?
- MCP defines a structured flow of data between agents. It ensures:
- Every agent receives input in a standardized format (e.g., query, chunks, metadata)
- Easy debugging, scaling, and maintenance of agent pipelines

## Demo Video
Watch the 5-minute demo showcasing ingestion, retrieval, and Q&A:
https://drive.google.com/file/d/1pEHqRpn0zz2wpuGn579QTAwSlBh_4ms6/view?usp=drive_link

## PPTX
https://docs.google.com/presentation/d/1MhTjOSUT6n0bwqvsGM76QtbImUEue0Jx/edit?usp=sharing&ouid=105552650117553750561&rtpof=true&sd=true

## Challenges Faced
- Optimizing inference speed on CPU-only systems (Intel Iris GPU, no NVIDIA CUDA support).
- Designing a flexible and clear communication protocol (MCP) for agent interaction.
- Parsing and normalizing multiple document formats with varying structures.
- Balancing retrieval relevance with prompt length constraints for LLM input.
- Managing multi-turn conversations with relevant source context display.

## Future Improvements
- Integrate GPU acceleration support (CUDA) for faster LLM inference.
- Add support for additional document types (e.g., HTML, EPUB).
- Implement caching strategies to speed up repeated queries.
- Expand MCP to support asynchronous and distributed agents.
- Enhance UI with richer context visualization and user feedback mechanisms.

## Contact
- Chakri Korsa
- chakrifavofvd@gmail.com
- +91 97044 10801
- Github-https://github.com/chakri970 | LinkedIn-https://www.linkedin.com/in/korsa-chakri-85782b256/




