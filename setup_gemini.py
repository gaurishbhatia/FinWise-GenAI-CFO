#!/usr/bin/env python3
"""
FinWise GenAI CFO - Gemini API Setup Guide
==========================================

This script provides a complete setup guide for using Gemini API with FinWise.
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

def main():
    print("=" * 70)
    print("FinWise GenAI CFO - Gemini API Setup Guide")
    print("=" * 70)
    
    print("\nSTEP 1: Get Your Gemini API Key")
    print("-" * 40)
    print("1. Visit: https://makersuite.google.com/app/apikey")
    print("2. Sign in with your Google account")
    print("3. Click 'Create API Key'")
    print("4. Copy the generated API key")
    
    print("\nSTEP 2: Configure Your Project")
    print("-" * 40)
    print("1. Open config.py")
    print("2. Replace 'your_gemini_api_key_here' with your actual API key")
    print("3. Save the file")
    
    print("\nSTEP 3: Run the Project")
    print("-" * 40)
    print("1. Open PowerShell/Command Prompt")
    print("2. Navigate to your project directory")
    print("3. Activate virtual environment: .\\venv\\Scripts\\Activate.ps1")
    print("4. Run: python src\\main_crew.py")
    
    print("\nSTEP 4: What You'll Get")
    print("-" * 40)
    print("- 6 AI agents working together")
    print("- Personalized financial planning")
    print("- Tax optimization recommendations")
    print("- Compliance verification")
    print("- Risk analysis and portfolio suggestions")
    print("- Professional financial report")
    
    print("\nIMPORTANT NOTES:")
    print("-" * 40)
    print("- Gemini API is FREE for most use cases")
    print("- No credit card required")
    print("- Generous rate limits")
    print("- High-quality AI responses")
    
    print("\nTROUBLESHOOTING:")
    print("-" * 40)
    print("If you get errors:")
    print("1. Make sure your API key is correct")
    print("2. Check your internet connection")
    print("3. Verify the virtual environment is activated")
    print("4. Run: pip install 'crewai[google-genai]'")
    
    print("\n" + "=" * 70)
    print("Ready to get started with FinWise!")
    print("=" * 70)

if __name__ == "__main__":
    main()
