#!/usr/bin/env python3
"""
Simple Gemini API Test
=====================
This script tests if your Gemini API key works correctly.
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

def test_gemini_api():
    print("Testing Gemini API...")
    
    try:
        from config import GEMINI_API_KEY
        
        if GEMINI_API_KEY == "your_gemini_api_key_here":
            print("ERROR: Please update config.py with your actual Gemini API key")
            print("Get your API key from: https://makersuite.google.com/app/apikey")
            return False
        
        # Test with CrewAI's Gemini integration
        from crewai.llm import LLM
        
        # Set environment variable
        os.environ['GOOGLE_API_KEY'] = GEMINI_API_KEY
        
        # Create Gemini LLM
        llm = LLM(model="gemini/gemini-1.5-pro")
        
        # Test a simple query
        response = llm.call("Hello, this is a test. Please respond with 'Gemini is working!'")
        
        print("SUCCESS: Gemini API is working!")
        print(f"Response: {response}")
        return True
        
    except Exception as e:
        print(f"ERROR: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure your API key is correct")
        print("2. Check your internet connection")
        print("3. Run: pip install 'crewai[google-genai]'")
        return False

if __name__ == "__main__":
    success = test_gemini_api()
    if success:
        print("\nYour FinWise project is ready to run!")
        print("Run: python src\\main_crew.py")
    else:
        print("\nPlease fix the issues above before running the main project.")
