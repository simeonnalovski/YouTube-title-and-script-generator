# YouTube-title-and-script-generator

In this project, I have used Streamlit for creating a simple Web UI and LangChain to create the Open AI model instance, chains and memory buffer.
The inteface has 3 key elements:
1. A slider, used for selecting the temprature of the model
2. A text input box, for inputing the topic
3. Two expanders for storing the previously generated titles and scripts from their memory (visible after the first use)

Lanchain was used for the following functionalities:
1. Creating the templates for title and script
2. Creating memory for titles and scripts
3. Generating the title and script for each promt
4. Creating a Open AI model instance

The project will generate the title and the script for YouTube videos based on two parameters:
1. The selected temperature (creativity) of the model, which you will selected by using the slider
2. The topic inputed via a text input box

How to use the project:
1. Clone the repository
2. Install the libraries
3. At line 14 replace YOUR_OPEN_AI_API_KEY with the value of your OpenAI API Key (preferably a paid API Key)
4. In your temrinal execute run streamlit app.py or run streamlit path
   NOTE: replace path with the filepath for app.py, if run streamlit app.py doesn't work
5. Open http://localhost:8501 to use it
6. By using the slider, adjust the temperature of the model, a decimal number between 0.1 and 1.0
7. Enter the topic in the text input box
8. Once you have written the topic, press Enter.
NOTE: After the first use the expanders will show the previously generated titles and scripts.
