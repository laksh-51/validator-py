# LLM-Based Input Validator

A production-grade Python script that leverages Gemini 2.5 Flash to validate user profile data. This project uses high-level prompt engineering instead of hardcoded logic to enforce data standards like E.164 and ISO-2.

## 🚀 Features
- **Zero-Library Logic**: All validation is handled by the LLM.
- **Structured Output**: Guaranteed JSON response format.
- **Automated Evals**: Integrated with `promptfoo` for testing.

## 🛠️ Setup Instructions

1. **Clone the project** and navigate to the directory:
   ```bash
   cd validator-py

2. **Create and activate a virtual environment:**

'''Bash

    cd python -m venv venv
    cd .\venv\Scripts\activate
    
3. **Install dependencies:**

'''Bash

    pip install -r requirements.txt
    npm install -g promptfoo

4. **Configure Environment: Create a .env file and add your Google Gemini API Key:**

'''Code snippet

    GEMINI_API_KEY=your_aiza_key_here   