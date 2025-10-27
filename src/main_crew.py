import sys
import os

# --- ADD THESE THREE LINES ---
# This ensures Python can find 'config.py' one level up in the parent directory.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from crewai import Agent, Crew, Process, Task
from config import GEMINI_API_KEY

# --- 1. Initialize Gemini LLM (Agent Brain) ---
# Simple approach: Use CrewAI's built-in Gemini support
try:
    # Try to use LangChain Google GenAI integration
    from langchain_google_genai import ChatGoogleGenerativeAI
    
    # Initialize Gemini LLM
    gemini_llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        google_api_key=GEMINI_API_KEY,
        temperature=0.7
    )
    print("Gemini LLM initialized successfully using LangChain")
    
except ImportError:
    print("LangChain Google GenAI not available, using CrewAI LLM...")
    
    # Use CrewAI's built-in LLM system
    from crewai.llm import LLM
    gemini_llm = LLM(model="gpt-3.5-turbo", api_key="dummy_key_for_testing")
    
except Exception as e:
    print(f"Error initializing Gemini: {e}")
    print("Using CrewAI LLM for testing...")
    
    # Use CrewAI's built-in LLM system
    from crewai.llm import LLM
    gemini_llm = LLM(model="gpt-3.5-turbo", api_key="dummy_key_for_testing")

# --- 2. Define Custom Tools (For Portfolio/Risk - Placeholder for later logic) ---

# Simple mock tool class
class MockTool:
    def __init__(self, name, func, description):
        self.name = name
        self.func = func
        self.description = description
    
    def run(self, *args, **kwargs):
        return self.func(*args, **kwargs)

def market_data_func(x: str = None) -> str:
    return "Simulated market data for S&P 500: +8.5% YTD. Real Estate: -2.0%."

market_data_tool = MockTool(
    name="Market Data Retriever",
    func=market_data_func,
    description="Gathers real-time (simulated) market data for major indices and assets.",
)

def monte_carlo_func(x: str = None) -> str:
    return "Monte Carlo simulation results: 82% probability of retirement success."

monte_carlo_tool = MockTool(
    name="Monte Carlo Simulator",
    func=monte_carlo_func,
    description="Runs 10,000 simulations against the proposed portfolio for risk quantification.",
)

# Mock RAG tools
def compliance_query_func(question: str) -> str:
    return f"Compliance check result for: {question}. Status: COMPLIANT (Source: SEC_Fiduciary_Duty_Rules.pdf)"

compliance_query_tool = MockTool(
    name="Compliance Auditor",
    func=compliance_query_func,
    description="Tool for querying the indexed SEC, FINRA, and legal compliance documents.",
)

def tax_query_func(question: str) -> str:
    return f"Tax optimization result for: {question}. Recommendation: Use Roth IRA (Source: IRC.pdf)"

tax_query_tool = MockTool(
    name="Tax Code Expert",
    func=tax_query_func,
    description="Tool for querying the indexed Internal Revenue Code (IRC) and IRS publications.",
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
    allow_delegation=False,
)

# 3. Tax Optimization Agent
tax_agent = Agent(
    role="Income and Asset Tax Minimizer",
    goal="Generate the most tax-efficient structure for all investments and income streams.",
    backstory="Focuses purely on minimizing lifetime tax liability through vehicles like Roth accounts, 529s, etc.",
    llm=gemini_llm,
    verbose=True,
    allow_delegation=True,
)

# 4. Risk & Simulation Agent
risk_agent = Agent(
    role="Monte Carlo & Economic Stress Tester",
    goal="Quantify risk by simulating thousands of economic futures and stress-testing the portfolio and generating risk narratives.",
    backstory="A quantitative modeling expert that tests worst-case scenarios and reports the probability of failure.",
    llm=gemini_llm,
    verbose=True,
)

# 5. Portfolio Allocation Agent
portfolio_agent = Agent(
    role="Tactical Investment Selector",
    goal="Translate high-level strategies into specific, low-cost investment instruments (ETFs, indices, etc.) that match the user's risk profile.",
    backstory="A tactical manager focused on efficient market access and rebalancing recommendations.",
    llm=gemini_llm,
    verbose=True,
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


# --- 4. Define the Tasks (The Complete 6-Step Workflow) ---

# Task 1: Strategy Creation
task_strategy = Task(
    description="Analyze the user's current profile (Age 30, Income $120k, Risk Moderate, Retirement Age 60). Draft a preliminary strategic plan covering debt reduction, optimal savings rate, and target asset allocation percentages.",
    agent=strategy_agent,
    expected_output="A preliminary 30-year financial plan with 5 key strategic pillars for growth and stability.",
)

# Task 2: Tax Optimization and Compliance Check (Uses RAG Tool: Tax Code Expert)
task_tax_check = Task(
    description="Review the high-level strategy from Task 1. Use the 'Tax Code Expert' tool to determine the most tax-efficient way to execute the savings plan (e.g., maximizing Roth vs. Traditional contributions). Report the precise IRC section used for justification.",
    agent=tax_agent,
    context=[task_strategy],
    expected_output="A detailed tax recommendation citing the specific IRC rule that supports the chosen retirement account structure.",
)

# Task 3: Compliance Validation (Uses RAG Tool: Compliance Auditor)
task_compliance_audit = Task(
    description="Audit the final Strategy and Tax recommendations from Task 1 & 2. Use the 'Compliance Auditor' tool to verify the advice meets Fiduciary Duty standards and SEC regulations. Generate a final Audit Trail with a Compliance Confidence Score (95%+ required).",
    agent=compliance_agent,
    context=[task_strategy, task_tax_check],
    expected_output="A final compliance sign-off with a verifiable Audit Trail and a Compliance Confidence Score.",
)

# Task 4: Risk Simulation and Stress Testing (Uses Tool: Monte Carlo Simulator)
task_risk_test = Task(
    description="Take the recommended portfolio allocation percentages and run a Monte Carlo simulation (use the 'Monte Carlo Simulator' tool). Also, generate a brief generative stress-test narrative (e.g., 'What happens if inflation hits 10%?'). Report the final probability of success.",
    agent=risk_agent,
    context=[task_strategy],
    expected_output="A risk report detailing the probability of retirement success and a summary of vulnerabilities under stress scenarios.",
)

# Task 5: Tactical Allocation and Instrument Selection (Uses Tool: Market Data Retriever)
task_portfolio_allocation = Task(
    description="Based on the strategy and risk report, use the 'Market Data Retriever' tool to select 5-7 specific, low-cost investment instruments (ETFs/Indices) that align with the moderate risk profile and current market trends. Provide a rationale for each selection.",
    agent=portfolio_agent,
    context=[task_strategy, task_risk_test],
    expected_output="A tactical list of 5-7 specific low-cost ETFs/Indices with detailed rationales for matching the strategy.",
)

# Task 6: Final Report Generation (Collects ALL outputs)
task_final_report = Task(
    description="Collect the outputs from all previous tasks (Strategy, Tax, Compliance Audit, Risk Report, Tactical List). Synthesize these into a single, cohesive, professional financial planning report, ready for export as a PDF/JSON.",
    agent=output_agent,
    context=[
        task_strategy,
        task_tax_check,
        task_compliance_audit,
        task_risk_test,
        task_portfolio_allocation,
    ],
    expected_output="A final, polished financial planning report containing all verified recommendations, the Compliance Audit Trail, and the Risk Simulation summary.",
)


# --- 5. Assemble and Run the Crew (Update the tasks list here) ---

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
        # The main sequential workflow
        tasks=[
            task_strategy,
            task_tax_check,
            task_compliance_audit,
            task_risk_test,
            task_portfolio_allocation,
            task_final_report,
        ],
        process=Process.sequential,  # Ensures audit happens before finalization
        verbose=True,
        manager_llm=gemini_llm,
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
