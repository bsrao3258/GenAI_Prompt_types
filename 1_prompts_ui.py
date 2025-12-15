from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",   # you can change the model name
    temperature=0.2
)

st.header('Research Tool')

user_input = st.text_input('Enter Your Prompt')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)


# to run this code use below command
# streamlit run 1_prompts_ui.py
