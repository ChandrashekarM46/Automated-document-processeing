import streamlit as st
import pytesseract
from PIL import Image
import openai
import os
from util import getCategory
from db import connectToDb

 openai.api_key = 'YOUR KEY'

# Set page title
st.set_page_config(page_title='OCR App')

# Set up sidebar
st.title('OCR App')


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Add file uploader
uploaded_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])

ocr_text = "" 
# Add OCR button
if st.button('Perform OCR'):

  # Check if file has been uploaded
  if uploaded_file is not None:
    with st.spinner("Extracting OCR..."):
    # Load image
      image = Image.open(uploaded_file)
      st.image(image)
      # Perform OCR using PyTesseract
      text = pytesseract.image_to_string(image)

      st.subheader("OCR Text")
      # Display OCR results
      with st.expander("See OCR Results"):
        st.write(text)

      #define the prompt
      ocr_text = text

      prompt= f"""Extract entities and their values from the provided text as a key-value pair, and separate them by a new line.
Text:{ocr_text} 
Entities:"""
      
      category=getCategory(ocr_text)
      st.title(category)

      connectToDb(uploaded_file.name,category)
      

# after obtaining the ocr text

# entitiy extraction using OpenAi
    response= openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    entities = response['choices'][0]['text']
    

    st.subheader("Entities")
    with st.expander("See Extracted Entities"):
      st.code(entities)


  else:
    st.warning('Please upload an image first.')
