import streamlit as st
import os
import openai
import numpy as np


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

if color == 'White':
    st.write('You selected White.')
    st.image(
    "src/white.png",
    caption='Dalle Shirt',
    width= 500,
    )
elif color == 'Black':
    st.write('You selected Black.')
    st.image(
    "src/black.png",
    caption='Dalle Shirt',
    width= 500,
    )
elif color == 'Gary':
    st.write('You selected Gary.')
    st.image(
    "src/gary.png",
    caption='Dalle Shirt',
    width= 500,
    )
else:
    st.write("You need select your creative background.")    
    

if color == 'White' and submit_button:
    st.write('You selected White.')
    st.image(
    "src/white.png",
    caption='Dalle Shirt',
    width= 100,
    )
elif color == 'Black' and submit_button:
    st.write('You selected Black.')
    st.image(
    "src/black.png",
    caption='Dalle Shirt',
    width= 100,
    )
elif color == 'Gary' and submit_button:
    st.write('You selected Gary.')
    st.image(
    "src/gary.png",
    caption='Dalle Shirt',
    width= 100,
    )
else:
    st.write("You need select your creative background.")

