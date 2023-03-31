import streamlit as st
import torch
import numpy as np
from PIL i

#Environment set up
pinekey = st.secrets['pinekey']
preprocess = Compose([
    Resize(256),
    CenterCrop(224),
    ToTensor(),
    Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
INDEX_NAME = 'image-search-clothes'

st.write('## squeezenet Visual Search')
st.write('# Upload Image')

#PineCone Initialize
# authenticate with Pinecone API, keys available at your project at https://app.pinecone.io
pinecone.init(
#     h.pinecone_api_key,
    pinekey,
    environment="us-west4-gcp"  # find next to API key in console
)

if INDEX_NAME not in pinecone.list_indexes():
    pinecone.create_index(name=INDEX_NAME, dimension=INDEX_DIMENSION)
index = pinecone.Index(INDEX_NAME)




#Upload image
uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'png', 'jpeg'])

_,col1,_ = st.columns([1,8,1])
with col1: 
    upload_method = st.radio("Select a way", ("From examples", "From local"))
    form = st.form(key='image-form')
    if upload_method == "From examples":
        image_input = form.selectbox('Select the image here:',
                                ['src/test1.jpg', 'src/test2.jpg', 'src/test3.jpg']
                               )
    else:
        image_input = form.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    topK = form.number_input('result number',
                                min_value=0,
                                max_value=20,
                             value =10,
                                help = 'Number of images in searching results')
    submit = form.form_submit_button('Submit')
    
    #Pinepone response & process
    query_embedding = model(preprocess(image).unsqueeze(0)).tolist()
    # response = index.query(query_embedding, top_k=4, include_metadata=True)
    response = index.query(query_embedding, top_k=4, include_metadata=True)
    
    #Process the image id and connecting to S3
    top_similar_imageId = []
    for i in response['matches']:
        top_similar_imageId.append(i['id'].split('.')[1])
    print(top_similar_imageId)
    
