# AI-Powered Code Optimization Tool

This tool analyzes Python code snippets to identify performance bottlenecks and provides optimization suggestions using the Groq API. The tool is built using Streamlit for a web-based interface that allows users to upload code snippets and view the analysis results.

## Table of Contents

1. [Introduction](#introduction)
2. [How to Run the Project](#how-to-run-the-project)
3. [Design Choices Made](#design-choices-made)
4. [Assumptions and Limitations](#assumptions-and-limitations)
5. [Screenshots](#screenshots)
6. [Evaluation Criteria](#evaluation-criteria)

## Introduction

This project aims to help developers optimize their Python code by highlighting potential performance bottlenecks. The tool takes a Python code snippet as input, analyzes it using static analysis techniques, and provides suggestions for optimization. The analysis includes measuring cyclomatic complexity using Radon and fetching optimization suggestions via the Groq API.

## How to Run the Project

### Prerequisites
- Python 3.6 or higher
- `Streamlit` library
- `Radon` library
- `Groq API` credentials (API key)

### Steps to Run Locally
1. **Clone the repository**:
   ```bash
   git clone <your-repo-URL>
   ```

2. **Navigate to the project directory**:
   ```bash
   cd AI_Code_Optimization_Tool
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```
   This command will start the web application. The tool can be accessed via your web browser at `http://localhost:8501`.

## Design Choices Made

- **Streamlit**:
  - **Reason**: Chosen for its simplicity and quick deployment capabilities. It allows for rapid prototyping and easy integration with Python scripts. Streamlit's built-in support for interactive elements (like forms and graphs) makes it an excellent choice for this project.
  - **Trade-offs**: While Streamlit is great for development, it might not scale well for large-scale deployments due to resource limitations.

- **Radon**:
  - **Purpose**: Used to analyze code complexity by measuring cyclomatic complexity, which indicates how complex a piece of code is. It helps in identifying bottlenecks where the code might be difficult to maintain or optimize.
  - **Implementation**: It’s invoked through a Python function in `analysis.py` and processes each code snippet uploaded through the Streamlit interface.

- **Groq API**:
  - **Purpose**: To provide specific optimization suggestions based on the analysis done by Radon. The Groq API fetches advice on how to refactor the code to improve performance.
  - **Assumptions**: Users need to have an API key from Groq API to get suggestions.

## Assumptions and Limitations

- **Assumptions**:
  - The tool assumes Python 3.6 or higher is installed on the system.
  - It assumes that users have a basic understanding of Python code and know how to interpret code analysis results.
  - The tool is limited to static analysis and does not simulate execution or measure runtime performance.

- **Limitations**:
  - Does not support non-Python code.
  - May not handle very large codebases efficiently.
  - The interface might be limited to simple textual feedback and suggestions.

## Screenshots

### 1. Main Interface:
![Main Interface](https://github.com/user-attachments/assets/71d9df9f-ab3d-463c-8df4-da1981594cfb)

- Description: This screenshot shows the main interface of the tool. Users can paste their Python code in the text box provided and click "ctrl+enter" to analyze.

### 2. Code Analysis Results:
![Code Analysis Results](https://github.com/user-attachments/assets/535906b9-eceb-4a8b-b61b-3cb003a3759c)

- Description: This screenshot displays the results of the code analysis, including identified bottlenecks and suggested optimizations.

### 3. Example Code and Results:
![Example Code and Results](https://github.com/user-attachments/assets/500d4ee1-e6cf-4fd2-8853-f3f6b8b325f3)

- Description: An example code snippet is analyzed, and the tool displays the bottlenecks and suggestions for improvement.
