import streamlit as st
import os
import openai
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# OpenAI API
openai.organization = st.secrets["org"]
openai.api_key = st.secrets["openaikey"]

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
    input_prompt = form.text_input(label='Customerize your creative!')
    submit_button = form.form_submit_button(label='Submit')

color_dict = {'White': 'src/white.png', 'Black': 'src/black.png', 'Gary': 'src/gary.png'}
mask_dict = {'White': 'src/whitemask.png', 'Black': 'src/blackmask.png', 'Gary': 'src/garymask.png'}
st.image(
color_dict[color],
caption='Dalle Shirt',
width= 500,
)

if  submit_button:
    st.write('You selected White.')
    response = openai.Image.create_edit(
    image=open(color_dict[color], "rb"),
    mask=open(mask_dict[color], "rb"),
    prompt=input_prompt,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img


# Report body
