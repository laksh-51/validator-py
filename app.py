import streamlit as st
import json
import os
from validate_user import validate_user # Reusing your core function
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="LLM Input Validator", page_icon="🛡️")

st.title("🛡️ LLM-Based Input Validator")
st.markdown("""
Automatically detecting errors and warnings in user profiles using advanced LLM inference
""")

# Sidebar for API Status
with st.sidebar:
    st.header("Settings")
    if os.getenv("GEMINI_API_KEY"):
        st.success("Gemini API Key Loaded")
    else:
        st.error("API Key Missing in .env")

# Input Section
st.subheader("Input Data")
tab1, tab2 = st.tabs(["Upload JSON", "Paste JSON"])

input_data = None

with tab1:
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")
    if uploaded_file is not None:
        input_data = json.load(uploaded_file)

with tab2:
    json_text = st.text_area("Paste JSON here:", height=200, placeholder='{"name": "Aarav", ...}')
    if json_text:
        try:
            input_data = json.loads(json_text)
        except json.JSONDecodeError:
            st.error("Invalid JSON format")

# Validation Execution
if input_data:
    if st.button("Validate Profile"):
        with st.spinner("LLM is analyzing data..."):
            result_raw = validate_user(input_data)
            result = json.loads(result_raw)
            
            st.divider()
            
            # Display Results
            if result.get("is_valid"):
                st.success("✅ Profile is Valid!")
            else:
                st.error("❌ Profile is Invalid")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Errors**")
                if result.get("errors"):
                    for err in result["errors"]:
                        st.write(f"- :red[{err}]")
                else:
                    st.write("None")
                    
            with col2:
                st.write("**Warnings**")
                if result.get("warnings"):
                    for warn in result["warnings"]:
                        st.write(f"- :orange[{warn}]")
                else:
                    st.write("None")

            st.subheader("Raw LLM Response")
            st.json(result)