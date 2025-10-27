#!/usr/bin/env python3
"""
FinWise Simple Demo
==================
A simplified version of the FinWise project that demonstrates the structure
without requiring external API calls.
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def main():
    print("=" * 60)
    print("FinWise GenAI CFO - Financial Planning System")
    print("=" * 60)
    print()
    
    print("Project Structure:")
    print("- Strategy Agent: Lead Financial Strategist")
    print("- Compliance Agent: SEC/Tax Compliance Auditor") 
    print("- Tax Agent: Income and Asset Tax Minimizer")
    print("- Risk Agent: Monte Carlo & Economic Stress Tester")
    print("- Portfolio Agent: Tactical Investment Selector")
    print("- Output Agent: Report Finalizer and Execution Logger")
    print()
    
    print("Sample Financial Plan for User Profile:")
    print("- Age: 30")
    print("- Income: $120k")
    print("- Risk Profile: Moderate")
    print("- Retirement Age: 60")
    print()
    
    print("1. STRATEGY CREATION")
    print("-" * 20)
    print("Preliminary 30-year financial plan with 5 key strategic pillars:")
    print("• Emergency Fund: 6 months expenses ($30k)")
    print("• Debt Reduction: Pay off high-interest debt first")
    print("• Retirement Savings: 15% of income ($18k/year)")
    print("• Tax-Advantaged Accounts: Maximize 401k and Roth IRA")
    print("• Investment Allocation: 70% stocks, 30% bonds")
    print()
    
    print("2. TAX OPTIMIZATION")
    print("-" * 20)
    print("Tax-efficient strategy:")
    print("• Maximize 401k contributions ($23k/year)")
    print("• Roth IRA contributions ($7k/year)")
    print("• Tax-loss harvesting opportunities")
    print("• HSA contributions if eligible")
    print("• Source: IRC Section 401(k) and 408A")
    print()
    
    print("3. COMPLIANCE AUDIT")
    print("-" * 20)
    print("Compliance check results:")
    print("• Fiduciary Duty: COMPLIANT")
    print("• SEC Regulations: COMPLIANT")
    print("• FINRA Rules: COMPLIANT")
    print("• Compliance Confidence Score: 98%")
    print("• Source: SEC Fiduciary Duty Rules")
    print()
    
    print("4. RISK SIMULATION")
    print("-" * 20)
    print("Monte Carlo simulation results:")
    print("• Probability of retirement success: 87%")
    print("• Worst-case scenario: 2008-style crash")
    print("• Stress test: 10% inflation impact")
    print("• Recommended adjustments: Increase emergency fund")
    print()
    
    print("5. PORTFOLIO ALLOCATION")
    print("-" * 20)
    print("Recommended investment instruments:")
    print("• VTI (Total Stock Market): 50%")
    print("• VXUS (International Stocks): 20%")
    print("• BND (Total Bond Market): 20%")
    print("• VNQ (Real Estate): 10%")
    print("• Total Expense Ratio: 0.05%")
    print()
    
    print("6. FINAL REPORT")
    print("-" * 20)
    print("Comprehensive financial plan summary:")
    print("• Total annual savings: $25k")
    print("• Projected retirement fund: $2.1M")
    print("• Tax savings: $3,200/year")
    print("• Risk-adjusted return: 7.2%")
    print("• Compliance status: VERIFIED")
    print()
    
    print("=" * 60)
    print("FinWise Demo Complete!")
    print("=" * 60)
    print()
    print("Next Steps:")
    print("1. Set up your Gemini API key in config.py")
    print("2. Run: python src/main_crew.py")
    print("3. The system will use real AI agents for personalized planning")

if __name__ == "__main__":
    main()
