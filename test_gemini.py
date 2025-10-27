#!/usr/bin/env python3
"""
Test script to verify Gemini API integration
"""

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

def test_gemini_import():
    print("Testing Gemini API integration...")
    
    try:
        import google.generativeai as genai
        print("✅ Google Generative AI imported successfully")
        
        # Test configuration
        from config import GEMINI_API_KEY
        print("✅ Config file imported successfully")
        
        if GEMINI_API_KEY == "your_gemini_api_key_here":
            print("⚠️  Please update config.py with your actual Gemini API key")
            return False
        
        # Configure Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        print("✅ Gemini configured successfully")
        
        # Test model creation
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Gemini model created successfully")
        
        # Test a simple generation
        response = model.generate_content("Hello, this is a test.")
        print(f"✅ Test response: {response.text[:50]}...")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_gemini_import()
    if success:
        print("\n🎉 Gemini API integration is working!")
    else:
        print("\n❌ Gemini API integration failed")
