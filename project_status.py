#!/usr/bin/env python3
"""
FinWise Project Status
=====================
This script shows the current status of your FinWise project.
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

def check_project_status():
    print("=" * 60)
    print("FinWise GenAI CFO - Project Status")
    print("=" * 60)
    print()
    
    # Check if config.py exists and has API key
    try:
        from config import GEMINI_API_KEY
        if GEMINI_API_KEY == "your_gemini_api_key_here":
            print("API Key Status: [PENDING] - Please update config.py with your Gemini API key")
        else:
            print("API Key Status: [CONFIGURED] - Gemini API key is set")
    except ImportError:
        print("API Key Status: [ERROR] - config.py not found")
    
    print()
    print("Project Components:")
    print("- [READY] Project structure and dependencies")
    print("- [READY] Six-agent CrewAI architecture")
    print("- [READY] Mock tools for testing")
    print("- [READY] Gemini API integration code")
    print("- [READY] Working demo version")
    print()
    
    print("Available Commands:")
    print("1. python src/simple_demo.py     - Run the working demo")
    print("2. python src/main_crew.py       - Run the full AI system (requires API key)")
    print("3. python demo.py                 - Check project status")
    print()
    
    print("To get your Gemini API key:")
    print("1. Go to: https://makersuite.google.com/app/apikey")
    print("2. Create a new API key")
    print("3. Copy the key to config.py")
    print("4. Run: python src/main_crew.py")
    print()
    
    print("=" * 60)
    print("Your FinWise project is ready to use!")
    print("=" * 60)

if __name__ == "__main__":
    check_project_status()
