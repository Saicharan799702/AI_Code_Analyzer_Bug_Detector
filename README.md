AI Code Analyzer & Bug Detector

An AI-powered application that analyzes source code, detects potential bugs, suggests improvements, and explains the code using a Large Language Model (LLM).

This project demonstrates how Generative AI can assist developers in reviewing and improving code automatically.

Features

Detects bugs and logical errors in code

Suggests improvements and best practices

Generates an optimized version of the code

Explains the code in simple language

Calculates approximate time complexity

Interactive web interface

Tech Stack

Python

Streamlit – Web interface

OpenAI API – Large Language Model

python-dotenv – Environment variable management

Project Structure
AI_Code_Analyzer_Bug_Detector
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
Installation

Clone the repository:

git clone https://github.com/Saicharan799702/AI_Code_Analyzer_Bug_Detector.git

Navigate to the project folder:

cd AI_Code_Analyzer_Bug_Detector

Install dependencies:

pip install -r requirements.txt
Environment Setup

Create a .env file in the project directory.

OPENAI_API_KEY=your_api_key_here

This keeps your API key secure and prevents it from being uploaded to GitHub.

Run the Application

Start the Streamlit app:

streamlit run app.py

Then open in your browser:

http://localhost:8501
Example Use Case

Input code:

for i in range(5)
print(i)

The AI detects the syntax error and suggests the corrected code:

for i in range(5):
    print(i)

It also explains the issue and provides optimization suggestions.

Learning Outcomes

This project demonstrates:

Integration of Large Language Models into applications

Prompt engineering techniques

Building AI-powered developer tools

Creating interactive AI applications using Streamlit

Future Improvements

Multi-language support (Python, Java, C++)

Automatic bug fixing with side-by-side comparison

Code quality scoring

Deployment on cloud platforms

Author

Sai Charan

B.Tech – Computer Science Engineering

GitHub:
https://github.com/Saicharan799702

License

This project is for educational and learning purposes.
