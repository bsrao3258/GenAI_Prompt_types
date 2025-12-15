from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)",
     "Long (detailed explanation)"]
)

# -------------------------------
# UPDATED PROMPT (CLEAN MATH VERSION)
# -------------------------------

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Format all mathematical expressions using compact inline notation without extra spaces.
  Example format: Attention(Q,K,V)=softmax(QKᵀ/√dₖ)V
- Avoid brackets like [ ... ]. Use clean inline text format.

2. Analogies:
- Use relatable analogies to simplify complex concepts when appropriate.

If certain information is not available in the paper, respond with "Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the selected explanation style and length.
""",
    input_variables=["paper_input", "style_input", "length_input"]
)

# Fill values
filled_prompt = template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=length_input
)

# Button action
if st.button('Summarize'):
    response = model.invoke(filled_prompt)
    st.write(response.content)

# to run this code use below command
# streamlit run 1_prompts_ui.py
