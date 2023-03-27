import streamlit as st
# import os
# import openai
# import torch
import numpy as np


st.write('## AIGC Image')
st.image(
    "src/test1data.jpeg",
    caption='Query the Data',
     use_column_width  = 'always',
)

# input GUI for user
_,col1,_ = st.columns([1,8,1])
_,col2,_ = st.columns([1,8,1])
col1, col2 = st.columns(2,gap = "medium")

with col1:
    st.markdown('#### Original Shirt')
    st.image(
    "src/test1.jpg.jpeg",
    caption='Dalle Shirt',
     use_column_width  = 'always',
    )
with col2:
    form = st.form(key='my_form')
    form.text_input(label='Enter some text')
    submit_button = form.form_submit_button(label='Submit')

    
    
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
