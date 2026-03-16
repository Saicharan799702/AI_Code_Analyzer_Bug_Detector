import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Function to review code
def review_code(code):

    prompt = f"""
You are a senior software engineer.

Analyze the following code and provide:

1. Bugs or errors
2. Improvements
3. Optimized version of the code
4. Time complexity
5. Simple explanation

Code:
{code}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# Streamlit UI
st.title("AI Code Reviewer")

st.write("Paste your code and AI will analyze it.")

code_input = st.text_area("Enter your code here")

if st.button("Analyze Code"):

    if code_input.strip() == "":
        st.warning("Please enter some code.")

    else:
        with st.spinner("Analyzing code..."):
            result = review_code(code_input)

        st.subheader("AI Analysis")
        st.write(result)