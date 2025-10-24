from crewai import Agent, Crew, Process, Task
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp import Tool
from config import GEMINI_API_KEY
from src.tools.rag_tool import (
    compliance_query_tool,
    tax_query_tool,
)  # <-- NEW: Import the RAG tools!

# --- 1. Initialize the LLM (Agent Brain) ---
gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=GEMINI_API_KEY)

# --- 2. Define Custom Tools (For Portfolio/Risk - Placeholder for later logic) ---
# NOTE: Replace 'lambda' functions later with actual Python logic/API calls
market_data_tool = Tool(
    name="Market Data Retriever",
    func=lambda x: "Simulated market data for S&P 500: +8.5% YTD. Real Estate: -2.0%.",
    description="Gathers real-time (simulated) market data for major indices and assets.",
)

monte_carlo_tool = Tool(
    name="Monte Carlo Simulator",
    func=lambda x: "Monte Carlo simulation results: 82% probability of retirement success.",
    description="Runs 10,000 simulations against the proposed portfolio for risk quantification.",
)


# --- 3. Define all Six Agents ---

# 1. Strategy Agent (Master Planner)
strategy_agent = Agent(
    role="Lead Financial Strategist",
    goal="Synthesize user inputs into a cohesive, multi-stage financial strategy (retirement, debt, goals).",
    backstory="Expert planner skilled at converting complex life goals into actionable financial roadmaps.",
    llm=gemini_llm,
    verbose=True,
    allow_delegation=True,
)

# 2. Regulatory Compliance Agent (Auditor)
compliance_agent = Agent(
    role="SEC/Tax Compliance Auditor",
    goal="Rigidly check all planning and allocation advice against real-time US tax code (IRC) and financial regulations (SEC, FINRA).",
    backstory="A specialized, risk-averse legal AI responsible for generating the final Audit Trail and Compliance Confidence Score.",
    llm=gemini_llm,
    verbose=True,
    tools=[compliance_query_tool],  # <-- Integrated RAG Tool
    allow_delegation=False,
)

# 3. Tax Optimization Agent
tax_agent = Agent(
    role="Income and Asset Tax Minimizer",
    goal="Generate the most tax-efficient structure for all investments and income streams.",
    backstory="Focuses purely on minimizing lifetime tax liability through vehicles like Roth accounts, 529s, etc.",
    llm=gemini_llm,
    verbose=True,
    tools=[tax_query_tool],  # <-- Integrated RAG Tool
    allow_delegation=True,
)

# 4. Risk & Simulation Agent
risk_agent = Agent(
    role="Monte Carlo & Economic Stress Tester",
    goal="Quantify risk by simulating thousands of economic futures and stress-testing the portfolio and generating risk narratives.",
    backstory="A quantitative modeling expert that tests worst-case scenarios and reports the probability of failure.",
    llm=gemini_llm,
    verbose=True,
    tools=[monte_carlo_tool, market_data_tool],  # <-- Integrated Simulation Tools
)

# 5. Portfolio Allocation Agent
portfolio_agent = Agent(
    role="Tactical Investment Selector",
    goal="Translate high-level strategies into specific, low-cost investment instruments (ETFs, indices, etc.) that match the user's risk profile.",
    backstory="A tactical manager focused on efficient market access and rebalancing recommendations.",
    llm=gemini_llm,
    verbose=True,
    tools=[market_data_tool],
)

# 6. Output & Execution Agent
output_agent = Agent(
    role="Report Finalizer and Execution Logger",
    goal="Format the final, compliant, and stress-tested advice into a professional PDF/JSON report, including the Audit Trail.",
    backstory="The final interface responsible for presenting results and managing cost/system logs.",
    llm=gemini_llm,
    verbose=True,
    allow_delegation=False,
)


# --- 4. Define the Tasks (The Workflow) ---
# This defines the order and collaboration required by the agents.

# Task 1: Strategy Creation
task_strategy = Task(
    description="Analyze the user's age (30), income ($120k), risk (moderate), and retirement goal (age 60). Draft a preliminary strategy covering debt, savings rate, and asset allocation percentages.",
    agent=strategy_agent,
    expected_output="A preliminary 30-year financial plan with 5 key strategic pillars.",
)

# Task 2: Tax Optimization and Compliance Check (Parallel/Sequential)
task_tax_check = Task(
    description="Review the strategy from Task 1. Use the 'Tax Code Expert' tool to find the most tax-efficient way to execute the savings rate (Roth vs. Traditional 401k/IRA). Report the IRC section used.",
    agent=tax_agent,
    context=[task_strategy],
    expected_output="A detailed tax recommendation citing the specific IRC rule that supports the chosen retirement account structure.",
)

# Task 3: Compliance Validation
task_compliance_audit = Task(
    description="Audit the final strategy and tax recommendations from Task 1 & 2. Use the 'Compliance Auditor' tool to verify the advice meets Fiduciary Duty standards and SEC regulations. Generate a Compliance Confidence Score (90-100%).",
    agent=compliance_agent,
    context=[task_strategy, task_tax_check],
    expected_output="A final compliance sign-off with an Audit Trail showing the SEC rules that were checked.",
)

# NOTE: Add four more tasks for Portfolio Allocation, Risk Simulation, and Final Output.


# --- 5. Assemble and Run the Crew ---

if __name__ == "__main__":
    financial_crew = Crew(
        agents=[
            strategy_agent,
            compliance_agent,
            risk_agent,
            tax_agent,
            portfolio_agent,
            output_agent,
        ],
        tasks=[
            task_strategy,
            task_tax_check,
            task_compliance_audit,
        ],  # Only using the first three for this example
        process=Process.sequential,  # Sequential ensures audit happens after strategy is drafted
        verbose=2,
        manager_llm=gemini_llm,  # Use a powerful model for management/delegation
    )

    # Kick off the execution of the crew
    print("--- Starting FinWise Financial Planning Crew ---")
    results = financial_crew.kickoff()

    print(
        "\n\n################################################################################"
    )
    print("## Final FinWise Output:")
    print(
        "################################################################################"
    )
    print(results)
