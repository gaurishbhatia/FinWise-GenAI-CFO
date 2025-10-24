# src/tools/rag_tool.py

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import (
    OpenAI,
)  # Note: LlamaIndex uses OpenAI naming, but you can configure it for Gemini

# --- Configuration ---
# Point to your data directory relative to the project root
COMPLIANCE_DIR = "data/compliance_docs"
TAX_DIR = "data/tax_docs"

# Note: You need to configure the LLM for LlamaIndex to use Gemini.
# A simple way for a project prototype is to use a local or cloud provider endpoint.
# For simplicity, we'll assume a standard setup using environment variables for the prototype.


def build_compliance_index():
    """Loads compliance documents and creates a searchable vector index."""
    if not os.path.exists(COMPLIANCE_DIR):
        print(f"Error: Compliance directory not found at {COMPLIANCE_DIR}")
        return None

    documents = SimpleDirectoryReader(COMPLIANCE_DIR).load_data()
    # Using default VectorStoreIndex for simplicity
    index = VectorStoreIndex.from_documents(documents)
    return index


def build_tax_index():
    """Loads tax documents and creates a searchable vector index."""
    if not os.path.exists(TAX_DIR):
        print(f"Error: Tax directory not found at {TAX_DIR}")
        return None

    documents = SimpleDirectoryReader(TAX_DIR).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index


# Build the indices once when the application starts
COMPLIANCE_INDEX = build_compliance_index()
TAX_INDEX = build_tax_index()

# --- Query Tools ---


def query_compliance_database(question: str) -> str:
    """
    TOOL: Searches the SEC/FINRA database to verify a rule or compliance status.
    Used by the Regulatory Compliance Agent.
    """
    if COMPLIANCE_INDEX is None:
        return "Compliance database unavailable."

    query_engine = COMPLIANCE_INDEX.as_query_engine()
    response = query_engine.query(question)

    # Return both the answer and the source node for auditing
    return (
        str(response)
        + f" (Source: {response.source_nodes[0].metadata.get('file_name', 'N/A')})"
    )


def query_tax_database(question: str) -> str:
    """
    TOOL: Searches the IRC/IRS database for tax code sections.
    Used by the Tax Optimization Agent.
    """
    if TAX_INDEX is None:
        return "Tax database unavailable."

    query_engine = TAX_INDEX.as_query_engine()
    response = query_engine.query(question)

    # Return both the answer and the source node for auditing
    return (
        str(response)
        + f" (Source: {response.source_nodes[0].metadata.get('file_name', 'N/A')})"
    )


if __name__ == "__main__":
    # Simple test for the index
    print("Compliance Index Ready. Testing query...")
    if COMPLIANCE_INDEX:
        result = query_compliance_database(
            "What is the fiduciary duty required for a registered investment advisor?"
        )
        print("Query Result:", result)
