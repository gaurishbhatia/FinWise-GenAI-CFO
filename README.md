# FinWise: Generative Agent for Hyper-Personalized Financial Planning and Compliance

## Project Summary (The Problem)

FinWise is a multi-agent AI system designed to solve the critical flaw in consumer financial advice: **the lack of auditable compliance and true hyper-personalization.** Current tools are generic and cannot handle complex tax situations or guarantee regulatory adherence.

## Six-Agent Architecture & Core Features

We use a specialized CrewAI framework to orchestrate six agents, ensuring speed, accuracy, and auditability.

| Agent | Core Function | GenAI Component |
| :--- | :--- | :--- |
| **Strategy Agent** | Core Plan Generation | Dynamic Planning |
| **Tax Optimization Agent** | Minimizes tax liability using real-time code. | Knowledge Grounding (RAG) |
| **Regulatory Compliance Agent** | Audits all advice against SEC/FINRA rules. | Automated Monitoring & Audit Trail |
| **Risk & Simulation Agent** | Runs Monte Carlo and Generative Stress Tests. | Parallel Execution |
| **Portfolio Allocation Agent** | Selects specific investment instruments (ETFs, etc.). | Tool-Use (Simulated Market APIs) |
| **Output & Execution Agent** | Generates professional reports (PDF/JSON) and manages costs. | Cost Control & Structured Output |

## Installation & Setup

1.  **Clone the Repository:** `git clone [Your HTTPS URL]`
2.  **Setup Environment:** `pyenv local 3.11.8`
3.  **Create Venv:** `python -m venv venv`
4.  **Activate:** `source venv/Scripts/activate`
5.  **Install Dependencies:** `pip install -r requirements.txt`

## Development Progress

- [x] Initial Repository and Environment Setup
- [x] Project Structure and Configuration Files (`src/`, `data/`, `config.py`)
- [ ] **NEXT:** Define all six Agent classes.
- [ ] **NEXT:** Implement Compliance RAG System.