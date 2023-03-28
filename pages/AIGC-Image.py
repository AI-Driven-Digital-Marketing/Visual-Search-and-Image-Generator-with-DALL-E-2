import streamlit as st
import os
import openai
import numpy as np


st.write('## AIGC Image')

# input GUI for user
_,col1,_ = st.columns([1,8,1])
_,col2,_ = st.columns([1,8,1])
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
    
#     st.markdown('#### Features')
#     if function_selection == 'Q1':
#         '''Find customers who have returned items more than 20% more often than the average customer returns for a
#         store in a given state for a given year.'''
#         form = st.form(key='Q1-form')
#         prompt = form.text_input('year',
#                                         min_value=1900,
#                                         max_value=2100,
#                                         value  = 2000,
#                                         help = 'Input value not in range.(Range: 1900~2100)')
#         submit = form.form_submit_button('Submit')  
#     else:
#         pass

