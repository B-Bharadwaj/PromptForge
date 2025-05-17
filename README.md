# 🛠️ PromptForge – Smart Summarizer

**PromptForge** is a customizable NLP summarizer tool powered by Hugging Face’s `google/flan-t5-xl` model. It allows users to upload or paste large text content and generate summaries in different formats — all styled by tone and audience preferences.

---

## 🚀 Features

- 📄 **Summarize Large Text** – Upload `.txt` files or paste content directly.
- 🎨 **Tone Control** – Choose how formal, technical, or creative the summary sounds.
- 👥 **Audience Awareness** – Adjust explanation style for a child, student, expert, etc.
- 🧾 **Flexible Format** – Get output as a paragraph, bullet points, or a one-liner.
- 🎚️ **Max Tokens & Temperature** – Fine-tune output length and randomness.
- 📦 **Streamlit App UI** – Clean, interactive frontend with sidebar controls.

---

## 🧠 Model Used

- [`google/flan-t5-xl`](https://huggingface.co/google/flan-t5-xl)  
  An instruction-tuned LLM that excels at summarization, explanation, and zero-shot reasoning.

---

## 📸 UI Preview

> Sidebar with tone, audience, and formatting controls + Main panel for input and summary.

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/promptforge.git
cd promptforge

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

##▶️ Run the App
streamlit run app.py

```
---

## 📁 Project Structure
promptforge/
├── app.py                      # Streamlit app
├── requirements.txt
├── promptforge/
│   ├── task_parser.py         # NLP task parser
│   └── template_engine.py     # Prompt templates

