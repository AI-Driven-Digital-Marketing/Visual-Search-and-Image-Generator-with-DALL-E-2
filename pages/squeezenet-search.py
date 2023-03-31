import streamlit as st
import torch
import numpy as np
from PIL import Image
st.write('## squeezenet Visual Search')
st.write('# Upload Image')

_,col1,_ = st.columns([1,8,1])

with col1:    
    form = st.form(key='image-form')
    upload_method = st.radio("Select a way", ("From examples", "From local"))
    if upload_method == "From examples":
        image_input = form.selectbox('Select the image here:',
                                ['src/test1.jpg', 'src/test2.jpg', 'src/test3.jpg']
                               )
        image = Image.open(image_input) 
    else:
        image = form.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        
    topK = form.number_input('result number',
                                min_value=0,
                                max_value=20,
                             value =10,
                                help = 'Number of images in searching results')
    submit = form.form_submit_button('Submit')
