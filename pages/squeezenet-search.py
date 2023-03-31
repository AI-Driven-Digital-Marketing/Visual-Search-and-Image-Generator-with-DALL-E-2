# import streamlit as st
# import torch
# import numpy as np

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


if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    
    #Pinepone response & process
    query_embedding = model(preprocess(image).unsqueeze(0)).tolist()
    # response = index.query(query_embedding, top_k=4, include_metadata=True)
    response = index.query(query_embedding, top_k=4, include_metadata=True)
    
    #Process the image id and connecting to S3
    top_similar_imageId = []
    for i in response['matches']:
    top_similar_imageId.append(i['id'].split('.')[1])
    print(top_similar_imageId)
    
