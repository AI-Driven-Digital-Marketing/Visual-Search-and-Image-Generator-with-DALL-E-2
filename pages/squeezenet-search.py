# import streamlit as st
# import torch
# import numpy as np
st.write('## squeezenet Visual Search')
st.write('# Upload Image')

uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
