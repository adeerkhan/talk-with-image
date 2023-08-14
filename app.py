from tempfile import NamedTemporaryFile
import streamlit as st
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from tools import ImageCaptionTool, ObjectDetectionTool


# intializing the agent
tools = [ImageCaptionTool(), ObjectDetectionTool()]

conversational_memory = ConversationBufferWindowMemory(
    memory_key= 'chat_history',
    k=5,
    return_messages=True
)

llm = ChatOpenAI(
    openai_api_key= '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',
    temperature=0,
    model_name = "gpt-3.5-turbo"
)

agent = initialize_agent(
    agent = "chat-conversational-react-description",
    tools = tools,
    llm = llm,
    max_iterations = 5,
    verbose = True,
    memory = conversational_memory,
    early_stoppy_method = 'generate'
)

# setting up the title
st.title('Ask something from the image')

# setting up the header
st.header("Please upload an image")

# upload the file
file = st.file_uploader(" ", type=["jpeg", "jpg", "png"])

if file:
    # displaying the image
    st.image(file, use_column_width=True)

    # text input for the question
    user_question = st.text_input('Ask a question from your image')
    with NamedTemporaryFile(dir='.') as f:
        f.write(file.getbuffer())
        image_path = f.name

        # write agent response
        if user_question and user_question != "":
            with st.spinner(text="In Progress..."):
                response = agent.run('{}, this is the image path: {}'.format(user_question, image_path))
                st.write(response)
