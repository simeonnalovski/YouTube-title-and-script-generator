#import libraries

import os
import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

#OPENAI API KEY
os.environ['OPENAI_API_KEY'] = 'YOUR_OPEN_AI_API_KEY'
# Simple UI
st.title('YouTube title and script generator')
slider_value = st.slider("Select the models creativity", min_value=0.1, max_value=1.0, value=0.5)
promt=st.text_input('Input the topic') 

# title and scrpit temllates

title_template = PromptTemplate(
    input_variables = ['topic'],
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template='write me a youtube video script based on this title TITLE: {title} '
)
#buffer memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# llm instance
llm = OpenAI(temperature=slider_value)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)
#title and script cahins



if promt:
    #generating title and script
    title=title_chain.run(promt)
    script=script_chain.run(title=title)

    #displaying title and script
    st.write(title)
    st.wrtie(script)

    #history of previous interactions

    with st.expander('Title History'):
        st.info(title_memory.buffer)

    with st.expander('Script History'):
        st.info(script_memory.buffer)
