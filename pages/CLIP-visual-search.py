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

st.write('## CLIP Visual Search')
device = 'cpu'
@st.cache_data
def read_file():
    with open('src/image_paths.txt', 'r') as f:
        selected_files = [line.strip() for line in f.readlines()]
    image_encodings = torch.load('src/image_features.pt', map_location=torch.device('cpu'))
    return selected_files, image_encodings

@st.cache_resource
def initialize():
    model = CLIPVisionModel.from_pretrained('openai/clip-vit-base-patch32')
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    return model, processor

@st.cache_resource
def initialize_s3():
    os.environ['AWS_ACCESS_KEY_ID'] = st.secrets['key_id']
    os.environ['AWS_SECRET_ACCESS_KEY'] = st.secrets['key_secret']
    os.environ['AWS_DEFAULT_REGION'] = st.secrets['region']
    s3 = boto3.client('s3')
    return s3

def CLIP_search(image, top_k):
    image_input = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        image_encoding = model(image_input['pixel_values'])
    similarity = F.cosine_similarity(image_encoding['pooler_output'], image_encodings, dim=1)
    topk_values, topk_indices = torch.topk(similarity, k=top_k)
    return topk_indices.numpy(), topk_values.numpy()



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

selected_files, image_encodings = read_file()
model, processor = initialize()

# GUI
_,col1,_ = st.columns([1,8,1])
_,col2,_ = st.columns([1,8,1])
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
with col2:
    #image = Image.open(image_input) 
    if image :
        st.image(image, caption='Uploaded image', use_column_width=True)
    if submit:
        topk_indices, topk_values = CLIP_search(image, topK)
        search_outputs = [selected_files[x] for x in topk_indices]
        #st.write(search_outputs) # not show image right now
        output_images = read_s3(search_outputs)
        n = 5
        img = 0
        cols = st.columns(n)
        while img <len(output_images):
            with cols[img%n]:
                st.image(output_images[img],caption = f'Similarity : {topk_values[img]:.2%}')
            img += 1
        
