# src/main_crew.py
from crewai import Agent, Crew, Process, Task
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY
from src.tools.rag_tool import query_compliance_database, query_tax_database

# 1. Initialize the LLM (Agent Brain)
gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=GEMINI_API_KEY)

# --- AGENT DEFINITIONS ---

# 1. Strategy Agent
strategy_agent = Agent(
    role="Lead Financial Strategist",
    goal="Synthesize user inputs into a cohesive, multi-stage financial strategy (retirement, debt, goals).",
    backstory="Expert planner skilled at converting complex life goals into actionable financial roadmaps.",
    llm=gemini_llm,
    verbose=True,
    allow_delegation=True,
)

# 2. Regulatory Compliance Agent
compliance_agent = Agent(
    role="SEC/Tax Compliance Auditor",
    goal="Rigidly check all planning and allocation advice against real-time US tax code (IRC) and financial regulations (SEC, FINRA).",
    backstory="A specialized, risk-averse legal AI responsible for generating the final Audit Trail and Compliance Confidence Score.",
    llm=gemini_llm,
    verbose=True,
    tools=[query_compliance_database],
    allow_delegation=False,
    # Note: This agent will be heavily customized with RAG in the next step.
)

# ... (Define the remaining four agents using the same structure)

# 3. Tax Optimization Agent
tax_agent = Agent(
    role="Income and Asset Tax Minimizer",
    goal="Generate the most tax-efficient structure for all investments and income streams.",
    backstory="Focuses purely on minimizing lifetime tax liability through vehicles like Roth accounts, 529s, etc.",
    llm=gemini_llm,
    verbose=True,
    tools=[query_tax_database],
    allow_delegation=True,
)

# 4. Risk & Simulation Agent
risk_agent = Agent(
    role="Monte Carlo & Economic Stress Tester",
    goal="Quantify risk by simulating thousands of economic futures and stress-testing the portfolio.",
    backstory="A quantitative modeling expert that tests worst-case scenarios and reports the probability of failure.",
    llm=gemini_llm,
    verbose=True,
)

# 5. Portfolio Allocation Agent
portfolio_agent = Agent(
    role="Tactical Investment Selector",
    goal="Translate high-level strategies into specific, low-cost investment instruments (ETFs, indices, etc.).",
    backstory="A tactical manager focused on efficient market access and rebalancing recommendations.",
    llm=gemini_llm,
    verbose=True,
)

# 6. Output & Execution Agent
output_agent = Agent(
    role="Report Finalizer and Execution Logger",
    goal="Format the final, compliant advice into professional PDF reports and machine-readable JSON files.",
    backstory="The final interface responsible for presenting results and managing cost/system logs.",
    llm=gemini_llm,
    verbose=True,
)

# --- CREW SETUP ---
# You would define the tasks and create the Crew object here.

if __name__ == "__main__":
    # Example Crew instantiation (will be expanded later)
    financial_crew = Crew(
        agents=[
            strategy_agent,
            compliance_agent,
            risk_agent,
            tax_agent,
            portfolio_agent,
            output_agent,
        ],
        tasks=[],  # Tasks will be added in the next sprint
        process=Process.sequential,  # Start with sequential flow
        verbose=2,
    )

    # results = financial_crew.kickoff()
    # print("\n\n################################################################################")
    # print("## Final FinWise Output:")
    # print("################################################################################")
    # print(results)
