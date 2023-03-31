import streamlit as st
import torch
import numpy as np
from PIL import Image
import pinecone
import torchvision
from torchvision.transforms import (
    Compose, 
    Resize, 
    CenterCrop, 
    ToTensor, 
    Normalize
)
import json
import streamlit as st
import os
import glob
import random
import shutil
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt
import torch.nn.functional as F
import torch
import boto3
import io
from concurrent.futures import ThreadPoolExecutor
from transformers import CLIPProcessor, CLIPVisionModel


#Environment set up
@st.cache_resource
def initialize_s3():
    os.environ['AWS_ACCESS_KEY_ID'] = st.secrets['key_id']
    os.environ['AWS_SECRET_ACCESS_KEY'] = st.secrets['key_secret']
    os.environ['AWS_DEFAULT_REGION'] = st.secrets['region']
    s3 = boto3.client('s3')
    return s3


def read_s3(file_paths):
    bucket_name = 'visualsearch7374'
    s3 = initialize_s3()
    
    def read_image(file_path):
        s3_response = s3.get_object(Bucket=bucket_name, Key=file_path)
        return s3_response['Body'].read()
    
    # use a thread pool to read the images in parallel
    with ThreadPoolExecutor() as executor:
        image_contents = list(executor.map(read_image, file_paths))
        
    # create image objects from the binary content 
    image_outputs = [Image.open(io.BytesIO(image_content)) for image_content in image_contents]
    return image_outputs

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
# uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'png', 'jpeg'])

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

    if image_input:
        image = Image.open(image_input) 
        st.image(image, width=400, caption='Uploaded image', use_column_width=False)   
    if submit:
        #Pinepone response & process
        model = torchvision.models.squeezenet1_1(pretrained=True).eval()
        query_embedding = model(preprocess(image).unsqueeze(0)).tolist()
        # response = index.query(query_embedding, top_k=4, include_metadata=True)
        response = index.query(query_embedding, top_k=4, include_metadata=True)

        #Process the image id and connecting to S3
        top_similar_imageId = []
        for i in response['matches']:
            top_similar_imageId.append(i['id'].split('.')[1])
            
        with open('src/path_store.json', 'r') as f:
            path_store = json.load(f)

        search_outputs = [path_store[x] for x in top_similar_imageId]
        #st.write(search_outputs) # not show image right now
        output_images = read_s3(search_outputs)
        n = 5
        img = 0
        cols = st.columns(n)
        while img <len(output_images):
            with cols[img%n]:
                st.image(output_images[img])
            img += 1
