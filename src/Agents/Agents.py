from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.Tools.Tools import web_serach, scrape_url
from dotenv import load_dotenv
import os
import streamlit as st


# Load local .env file (for local development)
load_dotenv()

# Get API key from environment or Streamlit Cloud secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

try:
    if "GROQ_API_KEY" in st.secrets:
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

# Validate API key
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Add it to your .env "
        "or Streamlit Cloud Secrets."
    )

# Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=GROQ_API_KEY
)



def Build_Scrape_Agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
    )

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.
Topic: {topic}
Research Gathered:
{research}
Structure the report as:
Introduction
Key Findings (minimum 3 well-explained points)
Conclusion
Sources (list all URLs found in the research)
Be detailed, factual and professional."""),
])

Writer_chain = writer_prompt | llm | StrOutputParser()


critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
