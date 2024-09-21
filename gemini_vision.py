# GEMINI is a LLM model of Google
# we're using streamlit library for both frontend and backend

import streamlit as st  # to work with frontend and backend
from dotenv import load_dotenv  # load_env is a function
import os
from PIL import Image

import google.generativeai as genai
# this library gives us the capability to interact 
# with the gemini model

load_dotenv()  
# as soon as we call this function all the contents 
# of the .env file got loaded in this file


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')  
# with the help of OS, we are accessing those variables
# print(GOOGLE_API_KEY)

genai.configure(api_key=GOOGLE_API_KEY) 
# connection with our API_KEY

def get_gemini_response(input_message,input_image):
    model = genai.GenerativeModel('gemini-1.5-flash')  
    # this gemini_model we want for interaction
    if input_message != "":
        response = model.generate_content([input_message,\
                input_image]) # passing data to gemini_model
    else:
        response = model.generate_content(input_image)

    return response.text   # return only text
    # gemini model also gives some other calculations, etc. 
    # but if only want text response from gemini_model


# FRONTEND --->
st.set_page_config(page_title='Generative AI Based ChatBot')
st.header('Gemini Based ChatBot👽')  #(window + ;)for emoji
input = st.text_input('Input prompt :',key='input') #input box
uploaded_file = st.file_uploader('Choose an image : ',\
                    type=['jpeg','jpg','png']) # file uploader

# displaying the user inputted image 
display_image = ''
if uploaded_file is not None:
    display_image = Image.open(uploaded_file)
    st.image(display_image,caption='uploaded image',\
                use_column_width=True)  
    
    #'caption' is basically a msg
    #'use_column_width' -> displaying the img in a bigger form

submit = st.button('Submit')   # submit box

# FRONTEND DONE

if submit:
    output = get_gemini_response(input_message=input, \
                input_image=display_image) #calling the function
    st.subheader('Your response is :')
    st.write(output)

