# 🔬 AI Research Assistant — Multi-Agent Research Automation

An AI-powered research automation system that uses multiple specialized AI agents to search for information, scrape relevant web content, generate detailed research reports, and evaluate the quality of the final output.

The system automates the research workflow through four stages: **Search → Scrape → Write → Critic**.

## 🚀 Overview

Researching a topic manually often requires searching multiple websites, extracting useful information, organizing findings, and reviewing the final report.

AI Research Assistant simplifies this process using a multi-agent architecture where each agent has a dedicated responsibility.

Simply enter a research topic, and the system automatically performs the research process and generates a structured report.

## ✨ Key Features

- **🔎 Search Agent:** Finds recent, relevant, and reliable information about a given topic.
- **🌐 Scrape Agent:** Selects relevant URLs and extracts detailed website content.
- **✍️ Writer Agent:** Generates structured research reports using collected information.
- **🧠 Critic Agent:** Reviews the generated report and provides feedback.
- **📊 Streamlit Dashboard:** Interactive interface for running and monitoring research.
- **📄 Report Export:** Download generated research reports in Markdown format.
- **📚 Research History:** View previously completed research topics during the session.
- **⚡ Automated Workflow:** Coordinates all four agents through a single pipeline.

## 🏗️ System Architecture

```text
             User Input
                  |
                  v
          Research Topic
                  |
                  v
          +---------------+
          | Search Agent  |
          +---------------+
                  |
                  v
          +---------------+
          | Scrape Agent  |
          +---------------+
                  |
                  v
          +---------------+
          |  Writer Agent |
          +---------------+
                  |
                  v
          +---------------+
          |  Critic Agent |
          +---------------+
                  |
                  v
          +---------------+
          | Final Report  |
          +---------------+
                  |
                  v
          Streamlit UI
          /           \
      View Report   Download
```

## 🛠️ Technology Stack

| Technology            | Purpose                                              |
| --------------------- | ---------------------------------------------------- |
| Python                | Core programming language                            |
| Streamlit             | Interactive web interface                            |
| AI Agents             | Automated research workflow                          |
| LangChain / LangGraph | Agent orchestration (if used in your implementation) |
| Web Search Tools      | Finding relevant information                         |
| Web Scraping Tools    | Extracting website content                           |
| LLM                   | Research report generation and evaluation            |
