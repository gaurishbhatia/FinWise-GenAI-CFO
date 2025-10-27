import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import (
    OpenAI,
)  # Used internally by LlamaIndex for some functions
from langchain_core.tools import Tool  # Needed for the agents to use the functions

# --- Configuration ---
COMPLIANCE_DIR = "data/compliance_docs"
TAX_DIR = "data/tax_docs"


# --- Index Building Function ---
def build_index(directory):
    """Loads documents from a directory and creates a searchable vector index."""
    if not os.path.exists(directory):
        print(f"Warning: RAG directory not found at {directory}")
        return None
    try:
        # SimpleDirectoryReader loads all .pdf, .txt, etc., from the directory
        documents = SimpleDirectoryReader(directory).load_data()
        index = VectorStoreIndex.from_documents(documents)
        return index
    except Exception as e:
        print(f"Error building index for {directory}: {e}")
        return None


# Build the indices once when the application starts
COMPLIANCE_INDEX = build_index(COMPLIANCE_DIR)
TAX_INDEX = build_index(TAX_DIR)

# --- Define the Query Functions (Tools) ---

# The compliance query tool will be used by the Regulatory Compliance Agent
compliance_query_tool = Tool(
    name="Compliance Auditor",
    func=lambda question: str(COMPLIANCE_INDEX.as_query_engine().query(question)),
    description="Tool for querying the indexed SEC, FINRA, and legal compliance documents. Use this to verify the legality and fiduciary status of any financial advice.",
)

# The tax query tool will be used by the Tax Optimization Agent
tax_query_tool = Tool(
    name="Tax Code Expert",
    func=lambda question: str(TAX_INDEX.as_query_engine().query(question)),
    description="Tool for querying the indexed Internal Revenue Code (IRC) and IRS publications. Use this to find specific tax rules, exemptions, and optimal account types (Roth vs. Traditional).",
)
