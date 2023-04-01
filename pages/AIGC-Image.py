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
with st.expander("About this app"):
    st.markdown(
        """
Why Dalle2?:
1.DALLE2 is a powerful language model that can generate high-quality text and image content based on textual input
The model is based on the GPT-3 architecture and has been trained on a large corpus of text and image data.
2.The primary usage of DALLE2 is in generating coherent and visually plausible images based on natural language prompts.
This can be useful in a variety of applications, such as generating images for creative projects, designing products and marketing materials, 
and creating custom avatars and other graphical assets for online content.

3.In this task, we use the Edit API of Dalle2:
Input1: original image(PNG, <4MB)
Input2: Mask image (PNG, <4MB)
Input3: Prompt(User type in front-end)
    """
    )
    st.write("")

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
    input_prompt = form.text_input(label='Let\'s Customerize your creative!')
    submit_button = form.form_submit_button(label='Submit')

color_dict = {'White': 'src/white.png', 'Black': 'src/black.png', 'Gary': 'src/gary.png'}
mask_dict = {'White': 'src/whitemask.png', 'Black': 'src/blackmask.png', 'Gary': 'src/garymask.png'}


if  submit_button:
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
    st.image(img, caption='Your Creative', width= 500)
else:
    st.image(color_dict[color],
    caption='Yours Dalle Shirt',
    width= 500,
    )


# Report body
