import pytesseract
from tqdm.auto import tqdm
import os
import numpy as np
# import streamlit as st

import pinecone
from sentence_transformers import SentenceTransformer
model_name = "all-minilm-l6-v2"
model = SentenceTransformer(model_name)


def getCategory(ocr_text):
    pinecone.init(api_key = "b60565d6-28e0-41c4-9be4-a77fd78d892c",environment = "us-west1-gcp-free")
    index = pinecone.Index('ocr-text')
    query = ocr_text
    xq = model.encode([query]).tolist()
    result = index.query(xq,top_k=1,include_metadata=True)
    category=result["matches"][0]["metadata"]["category"]
    # st.write(result)
    return category


