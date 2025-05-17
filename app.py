import streamlit as st
import datetime
from transformers import pipeline


# --- CONFIG ---
st.set_page_config(page_title="PromptForge", page_icon="🛠️", layout="wide")
st.title("🛠️ PromptForge – Smart Summarizer")

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-xl", device=-1)

model = load_model()

# --- SIDEBAR CONTROLS ---
st.sidebar.header("📋 Summary Settings")

tone = st.sidebar.selectbox("🎨 Tone", ["neutral", "friendly", "formal", "technical", "creative"])
audience = st.sidebar.selectbox("👥 Audience", ["general", "child", "student", "expert"])
summary_format = st.sidebar.selectbox("🧾 Format", ["Paragraph", "Bullet Points", "One-liner"])
max_tokens = st.sidebar.slider("🔢 Max Tokens", 50, 500, 300)
temperature = st.sidebar.slider("🌡️ Temperature", 0.0, 1.0, 0.7)
prompt_label = st.sidebar.text_input("🏷️ Label", placeholder="e.g., Physics Notes")
deterministic = st.sidebar.checkbox("🔒 Consistent Output", value=True)

# --- MAIN PANEL ---
st.subheader("📄 Upload or Paste Text to Summarize")

uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])
if uploaded_file:
    file_text = uploaded_file.read().decode("utf-8").strip()
else:
    file_text = st.text_area("✍️ Or paste your content here:", height=250)

# --- Bullet Formatter ---
def format_bullet_summary(text):
    import re

    # Remove duplicate bullets and normalize whitespace
    text = re.sub(r"(•\s*)+", "", text)
    text = re.sub(r"^\s*[-o•]+\s*", "", text, flags=re.MULTILINE)

    # Break into proper sentences using punctuation
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    # Remove duplicates and enforce minimum length
    seen = set()
    bullets = []
    for s in sentences:
        s = s.strip()
        if len(s) > 10 and s not in seen:
            seen.add(s)
            bullets.append(f"• {s}")

    return "\n\n".join(bullets)  # Add spacing between bullets


# --- GENERATE PROMPT & SUMMARY ---
if st.button("🚀 Summarize"):
    if not file_text:
        st.warning("Please upload or paste text first.")
    else:
        # Summary style instructions
        style_map = {
            "Paragraph": "Summarize the following clearly in a concise paragraph.",
            "Bullet Points": "Summarize the following as a list of clear bullet points. Each point should start with '•'.",
            "One-liner": "Summarize the following in one short sentence."
        }

        # Final prompt
        prompt = (
            f"You are a {tone} communicator summarizing this for a {audience}.\n"
            f"{style_map[summary_format]}\n\n"
            f"{file_text}"
        )

        # Generation config
        do_sample_flag = not deterministic  # Invert checkbox state
        generation_args = {
            "max_new_tokens": max_tokens,
            "do_sample": do_sample_flag,
            "temperature": temperature if do_sample_flag else 0.0
}



        with st.spinner("Generating summary..."):
            try:
                result = model(prompt, **generation_args)
                summary = result[0]["generated_text"]

                # --- OUTPUT ---
                st.subheader("🤖 Summary Output")
                if summary_format == "Bullet Points":
                    st.markdown(format_bullet_summary(summary))
                else:
                    st.success(summary)



                with st.expander("🧩 Summary Context"):
                    st.markdown(f"- **Tone**: `{tone}`")
                    st.markdown(f"- **Audience**: `{audience}`")
                    st.markdown(f"- **Format**: `{summary_format}`")
                    if prompt_label:
                        st.markdown(f"- **Label**: `{prompt_label}`")


            except Exception as e:
                st.error(f"❌ Model generation failed: {e}")
