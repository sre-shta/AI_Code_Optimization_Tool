import streamlit as st
from analysis import analyze_code_complexity, run_static_analysis, suggest_optimizations_with_groq
import plotly.graph_objects as go

st.title("AI-Powered Code Optimization Tool")
st.markdown(
    """
    Upload a code snippet to:
    1. Identify bottlenecks.
    2. Get optimization suggestions using Groq API.
    """
)

# User Input
code_input = st.text_area("Paste your Python code snippet:")

if code_input:
    st.subheader("Analysis Results")

    # Complexity Analysis
    st.write("### Code Complexity")
    complexity = analyze_code_complexity(code_input)
    st.json(complexity)

    # Static Analysis
    st.write("### Static Analysis")
    static_results = run_static_analysis(code_input)
    st.text("Pylint Results:")
    st.text(static_results["pylint"])
    st.text("Flake8 Results:")
    st.text(static_results["flake8"])

    # Optimization Suggestions
    st.write("### Optimization Suggestions (Groq API)")
    suggestions = suggest_optimizations_with_groq(code_input)
    for suggestion in suggestions:
        st.markdown(f"- {suggestion}")

    # Visualize Complexity
    st.write("### Complexity Visualization")
    fig = go.Figure(
        data=[
            go.Bar(
                x=[f["name"] for f in complexity["functions"]],
                y=[f["complexity"] for f in complexity["functions"]],
            )
        ]
    )
    fig.update_layout(
        title="Function Complexity",
        xaxis_title="Functions",
        yaxis_title="Cyclomatic Complexity",
    )
    st.plotly_chart(fig)
