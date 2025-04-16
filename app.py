import streamlit as st
from streamlit_extras.app_logo import add_logo
from openai import OpenAI
import json
import requests

st.set_page_config(page_title="OpenAI 4.1 Series Tester", layout="wide")

st.title("OpenAI 4.1 Series Tester")
st.divider()

st.markdown(
    """
<style>
#openai-4-1-series-tester {
    font-size: 1.75rem!important;
    font-weight: 700;
    padding: 1.25rem 0px 1rem;
}
.stSidebar a {
    font-weight: 700;
    color: rgb(255, 75, 75);
    text-decoration: none;
}
</style>
""",
    unsafe_allow_html=True,
)

# Sidebar for API key, endpoint and model selection
with st.sidebar:
    st.image("https://i.ibb.co/4nD4P7Nz/logo-white.png", width=150)
    url = "https://walterpinem.com/openai-gpt-4-1/"
    st.write("A Streamlit app to test the newly released GPT-4.1 models.")
    st.markdown("Read full tutorial [here](%s)." % url)
    st.divider()
    st.header("Configurations")
    api_key = st.text_input("OpenAI API Key", type="password")

    model_options = [
        "Select Model",
        "GPT 4.1",
        "GPT 4.1 Mini",
        "GPT 4.1 Nano"
    ]

    endpoint_type = st.radio(
        "API Endpoint",
        ["Chat Completions", "Responses (Direct API)"]
    )

    selected_model = st.selectbox("Select Model", model_options)

# Input area
user_prompt = st.text_area("", placeholder="Insert the prompt...", height=150)
submit_button = st.button("Generate Response", use_container_width=True, type="primary")

# Model ID mapping
model_mapping = {
    "GPT 4.1": "gpt-4.1-2025-04-14",
    "GPT 4.1 Mini": "gpt-4.1-mini-2025-04-14",
    "GPT 4.1 Nano": "gpt-4.1-nano-2025-04-14"
}

# Function to call OpenAI API using chat completions
def generate_chat_completion(prompt, model_id, api_key):
    try:
        client = OpenAI(api_key=api_key)

        # Using the chat completions endpoint
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the response content
        if hasattr(response, 'choices') and len(response.choices) > 0:
            return response.choices[0].message.content
        else:
            return "No response content available"

    except Exception as e:
        return f"Error: {str(e)}"

# Function to call the new responses API directly
def generate_direct_response(prompt, model_id, api_key):
    try:
        url = "https://api.openai.com/v1/responses"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "model": model_id,
            "input": prompt
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            response_json = response.json()

            # Extract the text from the output structure based on the sample response
            if "output" in response_json and len(response_json["output"]) > 0:
                content = response_json["output"][0].get("content", [])
                if content and len(content) > 0:
                    text_items = [item["text"] for item in content if item["type"] == "output_text"]
                    return "\n".join(text_items)

            # If we couldn't extract text in the expected format, return the full JSON for debugging
            return f"Received response but couldn't parse output text:\n{json.dumps(response_json, indent=2)}"
        else:
            return f"API Error ({response.status_code}): {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"

# Generate and display response
if submit_button:
    if api_key == "":
        st.error("Please enter your OpenAI API key")
    elif selected_model == "Select Model":
        st.error("Please select a model")
    elif user_prompt.strip() == "":
        st.error("Please enter a prompt")
    else:
        model_id = model_mapping[selected_model]

        with st.spinner(f"Generating response using {selected_model}..."):
            st.divider()

            if endpoint_type == "Chat Completions":
                response = generate_chat_completion(user_prompt, model_id, api_key)
            else:
                response = generate_direct_response(user_prompt, model_id, api_key)

            # Display the response
            st.markdown(response)

            # Show additional response details in an expander
            with st.expander("View Response Details"):
                st.text("Model: " + model_id)
                st.text("Endpoint: " + endpoint_type)
                st.text("Prompt: " + user_prompt)
