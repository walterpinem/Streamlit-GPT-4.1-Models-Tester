# Streamlit App to Test OpenAI’s GPT-4.1 Models
A Python Streamlit application to test OpenAI's GPT-4.1 model series via OpenAI API, allowing you to test and compare different model variants with a user-friendly and simple interface.

![A Simple Python Streamlit App for Testing Grok GPT-4.1 Models](https://walterpinem.com/wp-content/uploads/2025/04/OpenAI-GPT-4.1-Series-Python-Streamlit.png)

#### Simple usage:

    streamlit run app.py

---
Here’s how you can get started:

#### **1\. Create a Python Virtual Environment**

Open your terminal (or Command Prompt on Windows) and navigate to your project directory. Then run:

##### Windows & Mac

    python -m venv gpt4_1_env
    

Activate it by running: 

**On Windows:**

    gpt4_1_env\Scripts\activate
    

**On macOS/Linux:**

    source gpt4_1_env/bin/activate
    

For more detailed cover up, learn my post about [**Python virtual environment**](https://walterpinem.com/python-virtual-environment/).

#### **2\. Install Required Packages**

With your virtual environment activated, install Streamlit and [**OpenAI Python SDK**](https://github.com/openai/openai-python) as Grok xAI API is compatible with OpenAI (as well as any other dependencies you need) using `pip`:

    pip install streamlit openai
    
This will install the Streamlit framework, which we use to build our interactive web app, and the OpenAI package, which is required to interact with the Grok xAI API.

Read the full explanation and tutorial on [**Build a Streamlit App to Test OpenAI’s GPT-4.1 Models**](https://walterpinem.com/openai-gpt-4-1/).
