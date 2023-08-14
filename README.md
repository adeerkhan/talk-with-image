# Talk with your image using Streamlit and LangChain

Welcome to the Talk with your image repository! This project showcases a powerful Streamlit application that allows users to ask questions about images they upload and receive insightful responses from an AI conversational agent. The heart of this app is the OpenAI GPT-3.5 Turbo model, which harnesses advanced language capabilities to provide accurate answers based on both the uploaded image and user queries.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/talk-with-image.git
    ```
   
2. **Navigate to the Project Directory:**

    ```bash
    cd talk-with-image
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Get Your OpenAI API Key:**

    Sign up for an API key at [OpenAI](https://platform.openai.com).

5. **Configure Your API Key:**

    Replace the placeholder API key in `app.py` with your actual OpenAI API key:

    ```python
    llm = ChatOpenAI(
        openai_api_key='YOUR_API_KEY',
        temperature=0,
        model_name="gpt-3.5-turbo"
    )
    ```

6. **Run the Streamlit Application:**

    ```bash
    streamlit run main.py
    ```

7. **Access the Application:**

    Open your web browser and navigate to http://localhost:8501 to explore the application.

## Usage

1. **Upload an Image:**

    Click the file upload button to upload an image.

2. **Display of Uploaded Image:**

    The uploaded image will be displayed on the interface.

3. **Ask a Question:**

    Enter a question related to the image in the provided text input field.

4. **AI Response:**

    The AI conversational agent will generate a response based on your question and the image.

5. **View Response:**

    The generated response will appear below the question input area.

## Included Tools

This application comes with the following valuable tools:

- **ImageCaptionTool:**
    Generates descriptive captions for the uploaded images.

- **ObjectDetectionTool:**
    Performs object detection on the uploaded images, identifying the objects present.

## Contribution

Contributions to this project are greatly appreciated! If you have any ideas, improvements, or bug fixes, don't hesitate to submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- The OpenAI GPT-3.5 Turbo model powers the AI conversational agent. Learn more at [OpenAI](https://openai.com/).
- The interactive user interface is built using the Streamlit library. Refer to the [Streamlit documentation](https://docs.streamlit.io/) for details.
- The LangChain library manages the conversational AI agent and tools. Find more information at the [LangChain GitHub repository](https://github.com/hwchase17/langchain).
- The Transformers library facilitates AI inference. Further details about the models used can be found [here](https://huggingface.co/Salesforce/blip-image-captioning-large) and [here](https://huggingface.co/facebook/detr-resnet-50).
- The above repository has been made from the following [repository](https://github.com/computervisioneng/ask-question-image-web-app-streamlit-langchain) and [tutorial](https://www.youtube.com/watch?v=71EOM5__vkI)
---

Feel free to modify and personalize the content to fit your repository's specific details. Happy coding!
