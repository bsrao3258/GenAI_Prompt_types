# 📘 Research Paper Summarization App

A Streamlit-based interactive tool that summarizes research papers using OpenAI + LangChain.


## 🔧 **Step 1: Create `.env` File**

Create a `.env` file in your project root and paste your OpenAI API key:

```env
OPENAI_API_KEY=xxxxx
```

> ⚠️ **Important:**
> Do **not** add quotes around the key.



## 📦 **Step 2: Install Required Python Libraries**

### Option A — Install using `requirements.txt`

```bash
pip install -r requirements.txt
```

### Option B — Install manually

```bash
pip install streamlit python-dotenv langchain-openai langchain-core langchain-community openai
```



## ▶️ **Step 3: Run the Application**

```bash
streamlit run 2_prompts_ui_dynamic.py
```



## 🌐 **Access the UI**

Once the app starts, Streamlit will open the UI automatically in your default browser:

```
http://localhost:8501/
```

Use the browser interface to:

* Select a research paper
* Choose explanation style
* Choose summary length
* Generate summaries with clean mathematical expressions and analogies

---

## 📝 Notes

* Ensure `.env` exists before running the app
* Your OpenAI API key should have valid usage quota
* You can stop the app anytime using `CTRL+C` in the terminal

