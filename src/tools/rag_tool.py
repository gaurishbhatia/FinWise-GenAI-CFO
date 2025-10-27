import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from crewai_tools import Tool

Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
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


def query_compliance_database_func(question: str) -> str:
    """
    Searches the SEC/FINRA database to verify a rule or compliance status.
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
    pass


compliance_query_tool = Tool(
    name="Compliance Auditor",
    func=query_compliance_database_func,
    description="Tool for querying the indexed SEC, FINRA, and legal compliance documents. Use this to verify the legality and fiduciary status of any financial advice.",
)


def query_tax_database_func(question: str) -> str:
    """
    Searches the IRC/IRS database for tax code sections.
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
    pass


tax_query_tool = Tool(
    name="Tax Code Expert",
    func=query_tax_database_func,
    description="Tool for querying the indexed Internal Revenue Code (IRC) and IRS publications. Use this to find specific tax rules, exemptions, and optimal account types (Roth vs. Traditional).",
)


# # Note: The query tool names used in main_crew.py are now the decorated functions themselves.
# compliance_query_tool = query_compliance_database_func
# tax_query_tool = query_tax_database_func
