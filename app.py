from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
import streamlit as st
model = genai.GenerativeModel('gemini-1.5-flash-002')

print(dir(model))
genai.configure(api_key=os.getenv("gkey"))
model=genai.GenerativeModel("models/gemini-pro")
#print(dir(list(model)))
#function for load gemini pro model and get response
def get_gemini_response(questions):
    response=model.generate_content(questions)
    return response.text
#initization of streamlit app
st.set_page_config(page_title="quizz")
st.header('gemini llm application')
input=st.text_input("input",key="input")
submit=st.button("ASk a question??")
#submitted click
if submit:
    response=get_gemini_response(input)
    st.subheader("the header is ")
    st.write(response)