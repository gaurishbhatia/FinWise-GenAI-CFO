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
        
        # Test with direct Google Generative AI
        import google.generativeai as genai
        
        # Configure Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Create Gemini model
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        # Test a simple query
        response = model.generate_content("Hello, this is a test. Please respond with 'Gemini is working!'")
        
        print("SUCCESS: Gemini API is working!")
        print(f"Response: {response.text}")
        return True
        
    except ImportError:
        print("ERROR: Google Generative AI not installed")
        print("Run: pip install google-generativeai")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure your API key is correct")
        print("2. Check your internet connection")
        print("3. Run: pip install google-generativeai")
        return False

if __name__ == "__main__":
    success = test_gemini_api()
    if success:
        print("\nYour FinWise project is ready to run!")
        print("Run: python src\\main_crew.py")
    else:
        print("\nPlease fix the issues above before running the main project.")
