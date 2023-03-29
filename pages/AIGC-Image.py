import streamlit as st
import os
import openai
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# OpenAI API
openai.organization = "org-hZCjhqvXmAGGiwqIXIzozujs"
openai.api_key = "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"


# Tittl 
st.write('## AIGC Image')
# input GUI for user
_,col1,_ = st.columns([1,6,1])
_,col2,_ = st.columns([1,6,1])
col1, col2 = st.columns(2,gap = "medium")

with col1:
    st.markdown('#### Original Creative')
    
    color = st.radio(
    "Select your shirt color:",
    ('White', 'Black', 'Gary'))

with col2:
    form = st.form(key='my_form')
    form.text_input(label='Customerize your creative!')
    submit_button = form.form_submit_button(label='Submit')

if color == 'White' and submit_button:
    st.write('You selected White.')
    st.image(
    "src/white.png",
    caption='Dalle Shirt',
    width= 500,
    )
elif color == 'Black' and submit_button:
    st.write('You selected Black.')
    st.image(
    "src/black.png",
    caption='Dalle Shirt',
    width= 500,
    )
elif color == 'Gary' and submit_button:
    st.write('You selected Gary.')
    st.image(
    "src/gary.png",
    caption='Dalle Shirt',
    width= 500,
    )
else:
    st.write("You need select your creative background.")    


# Report body
response = openai.Image.create_edit(
  image=open("src/white.png", "rb"),
  mask=open("src/whitemask.png", "rb"),
  prompt="A brutalism building by the sea.",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img