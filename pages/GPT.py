import streamlit as st
from openai import OpenAI

page_title="GPT"
st.set_page_config(page_title=page_title, page_icon="🤖", layout="wide")
st.title(page_title)


# st.set_page_config(layout="wide")


# st.write('http://localhost:8501')
# st.write('http://localhost:8501/?openai_api_key=testing_retrival_of_key')
# st.write('http://localhost:8501/?openai_api_key=testing_retrival_of_key&key_description=descripion_here')


api_key = st.query_params.get("openai_api_key", "<Paste your OpenAI api Key here, but remember to set a spending limit for it first>")
key_description = st.query_params.get("key_description", "")


with st.expander(f'Details:', False):
    api_key_input = st.text_input('Enter your API Key:', value=api_key)
    st.write(f'OpenAI API Key: {api_key_input}')
    st.write(f'Key description: {key_description}')


client = OpenAI(api_key=api_key_input)


def get_openai_response(messages, model):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True
    )
    return response


# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# if "user_message" not in st.session_state:
#     st.session_state.user_message = ""


options = ["gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5"]
selected_model = st.selectbox("Model:", options)
# st.write(f"Selected model: {selected_model}")


def submit_message(placeholder_question, placeholder_answer):
    user_message = st.session_state.user_message
    if user_message:
        # Append user's message to a temporary chat history
        temp_chat_history = st.session_state.chat_history + [{"role": "user", "content": user_message}]

        placeholder_question.write("**User:**\n" + user_message)

        try:
            # Get response from OpenAI
            with st.spinner("Generating response..."):
                response = get_openai_response(temp_chat_history, selected_model)
                response_text = ""
                for chunk in response:
                    content = chunk.choices[0].delta.content
                    if content:
                        response_text += content
                        placeholder_answer.write("**Assistant:**\n" + response_text) # Update the placeholder with the current content
                
                st.session_state.chat_history.append({"role": "user", "content": user_message})
                st.session_state.chat_history.append({"role": "assistant", "content": response_text})

                # Clear the user input
                # st.session_state.user_message = ""
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            # Do not clear the user input to allow retry

# Display the chat history
st.subheader("Chat History")
for message in st.session_state.chat_history:
    role = message["role"]
    content = message["content"]
    if role == "user":
        st.write("**User:**")
    else:
        st.write("**Assistant:**")
    st.write(content)


placeholder_question = st.empty()
placeholder_answer = st.empty()

# Text area for the user to input their message
st.text_area("Your message:", key="user_message")

# Submit button
if st.button("Submit"):
    submit_message(placeholder_question, placeholder_answer)

