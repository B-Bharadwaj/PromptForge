# app.py

import streamlit as st
from promptforge.task_parser import parse_task_description
from promptforge.template_engine import select_template

st.set_page_config(page_title="PromptForge", page_icon="🛠️", layout="wide")
st.title("🛠️ PromptForge – Auto Prompt Generator")

# User input
task_input = st.text_area("🧾 Describe your NLP task here (e.g., 'Summarize this blog for kids')")

if st.button("⚙️ Generate Prompt"):
    if not task_input.strip():
        st.warning("Please enter a task description.")
    else:
        # Step 1: Parse
        parsed = parse_task_description(task_input)

        # Step 2: Select prompt
        template = select_template(parsed)

        # Step 3: Replace placeholder
        final_prompt = template.replace("{input}", "[Paste your input here]")

        st.subheader("🧠 Generated Prompt:")
        st.code(final_prompt, language="markdown")

        st.info(f"🧩 Parsed task → Type: `{parsed['task_type']}`, Tone: `{parsed['tone']}`, Audience: `{parsed['audience']}`")
