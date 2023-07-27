import streamlit as st
import pytesseract
from PIL import Image
import openai
import os
from util import getCategory
from db import connectToDb

# from dotenv import load_dotenv
# load_dotenv()

# openai.api_key = ''

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
# import subprocess
# import json

# # Save OCR results to ocr_result.txt
# with open('ocr_result.txt', 'w') as file:
#     file.write(ocr_text)

# # Execute testing.ipynb
# try:
#     subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', 'testing.ipynb'])
# except subprocess.CalledProcessError as e:
#     # Handle the exception (e.g., print an error message or take alternative actions)
#     st.warning("Error executing testing.ipynb:", e)


# # Load the updated category from category.txt
# try:
#     with open('category.txt', 'r') as file:
#         category = json.load(file)
# except json.JSONDecodeError as e:
#     st.error('Error loading JSON: ' + str(e))

# # Check if category is not None
# if category is not None:
#     # Use the loaded category variable in your code
#     st.warning(category)


# import subprocess
# subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', 'testing.ipynb'])
# #Now you can use the category variable in main.py
# st.warning(category)


# After obtaining the ocr_text variable

      #Get The Response
#     response= openai.Completion.create(
#     model="text-davinci-003",
#     prompt=prompt,
#     temperature=0,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )
#     entities = response['choices'][0]['text']
    

#     st.subheader("Entities")
#     with st.expander("See Extracted Entities"):
#       st.code(entities)


  # else:
  #   st.warning('Please upload an image first.')
