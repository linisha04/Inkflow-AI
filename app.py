import pandas as pd 
import numpy as np 
import os
from secret_key import api_key
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate


os.environ["HUGGINGFACEHUB_API_TOKEN"]=api_key

repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"
# repo_id="mistralai/Mistral-7B-Instruct-v0.3"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_length=128,
    temperature=0.5,
    huggingfacehub_api_token=api_key,
)


p_template=PromptTemplate(

    input_topic=['topic'],
    template='''
    I want to write a good blog on the topic: {topic}.
    The title can be Informative, Humorous, or Persuasive.
    The target audience is Beginners, Intermediate, or Experts.
    Suggest a list of 5 creative titles for the blogs.
    Format the response as:
    - Title 1
    - Title 2
    - Title 3
    - Title 4
    - Title 5
    '''
    


    )



prompt_temp_blog= PromptTemplate(

    input_variables=['blog_title','keywords','blog_length' ] ,
    template='''

    Write a high-quality , informative , plagiarism-free blog post  on the topic {blog_title}.
    Target the content towards a beginner audience.
    Use a conversational wrtiting style and struture the content with introduction,body paragraphs and conclusion.
    Try to include the following keywords in the blog post : {keywords}.
    Aim for a blog length of {blog_length} words.
    Make the content complete, engaging , catches the readers attention and easy to understand stricly follow the struction consisting for blog's introdution , blog's paragraphs , blog's conclusion .
    '''

    )

title_chain=p_template | llm

blog_chain=prompt_temp_blog | llm


import streamlit as st

st.title("InkFlowAI.....Blog Creation Assistant🤖")
st.subheader("Create high-quality blog post with ease using InkflowAI")

st.subheader("Generate Creative Blog Titles")
topic_expander=st.expander('Input the topics on which you want to generate blog.')

with topic_expander:
    topic=st.text_input("Enter the topic for which you want to generate blog titles" , key='topic')
    if st.button("Generate Blog Titles"):
        titles=title_chain.invoke({topic})
        st.write(titles)

st.subheader("Generate Blog Post")

blog_expander=st.expander('Input the details for generating blog post')

with blog_expander:
    blog_title=st.text_input("Enter the topic for which you want to generate blog post" , key='blog_title')

    blog_length=st.slider("Enter the blog length" ,min_value=50 , max_value=1000 , key='blog_length' ,step=50)
    
    if 'keywords' not in st.session_state:
        st.session_state.keywords=[]
    keyword_input=st.text_input("Enter the keyword")
    keyword_button=st.button("Add Keyword")
    if keyword_button:
        st.session_state.keywords.append(keyword_input)        
        st.session_state['keyword_input']=""
        for keyword in st.session_state['keywords']:
            st.write(f"<div style='display:inline-block ; background-color=light-gray ; padding:5px ; margin:5px;'>{keyword}</div>",unsafe_allow_html=True) 
            
    
   
    if st.button("Generate Blog Post"):
        formatted_keywords=",".join(st.session_state.keywords)
        st.subheader(blog_title)
        blog=blog_chain.invoke({"blog_title":blog_title,"keywords":formatted_keywords,"blog_length":blog_length})
        st.write(blog)


        #;