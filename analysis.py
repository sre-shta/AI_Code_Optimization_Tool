import os
import radon.complexity as radon_complexity
import subprocess
from typing import Dict, List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def analyze_code_complexity(code: str) -> Dict:
    """
    Analyzes code for cyclomatic complexity using Radon.
    """
    blocks = radon_complexity.cc_visit(code)
    return {
        "total_complexity": sum(block.complexity for block in blocks),
        "functions": [
            {"name": block.name, "complexity": block.complexity} for block in blocks
        ],
    }

def run_static_analysis(code: str) -> Dict:
    """
    Runs Pylint and Flake8 for static code analysis.
    """
    with open("temp_code/temp_code.py", "w") as f:
        f.write(code)

    pylint_result = subprocess.run(
        ["pylint", "temp_code/temp_code.py"], capture_output=True, text=True
    )
    flake8_result = subprocess.run(
        ["flake8", "temp_code/temp_code.py"], capture_output=True, text=True
    )

    return {
        "pylint": pylint_result.stdout,
        "flake8": flake8_result.stdout,
    }

def suggest_optimizations_with_groq(code: str) -> List[str]:
    """
    Uses Groq API to suggest code optimizations.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Please check your .env file.")

    # Mock API interaction (replace with actual Groq API calls)
    # TODO: Integrate real Groq SDK/API calls.
    mock_response = [
        "Consider breaking large functions into smaller ones.",
        "Optimize nested loops to improve performance.",
        "Avoid global variables; use local variables where possible.",
    ]
    return mock_response
