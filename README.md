# Visual-Search
[![author](https://img.shields.io/badge/Author-Rayden_Xu-blue.svg)](https://www.linkedin.com/in/rundong-xu-269012230/) 
[![author](https://img.shields.io/badge/Author-Binghui_Lai-blue.svg)](https://www.linkedin.com/in/binghui-lai/) 
[![author](https://img.shields.io/badge/Author-Ziwei_Duan-blue.svg)](https://www.linkedin.com/in/ziwei-duan-create/) 
## Quick Portral
### 
| **--->** [1.Streamlit App](https://dduan-zw-visual-search-welcome-fztyvt.streamlit.app/) |

| **--->** [2.Codelab](https://docs.google.com/document/d/1p8RdCUnfBQIfVtpQ8gmEty_1RgeEwW62a6ZI0g2rdaI/edit#heading=h.knzgz5vyduac) |

## Introduction
#### What is Image Search and how will we use it?
One may find themselves with an image, looking for similar images among a large image corpus. The difficult part of this requirement is instantly retrieving, at scale, similar images, especially when there are tens of millions or billions of images from which to choose.

In this repo, we will walk you through the mechanics of how to solve this problem using an off-the-shelf, pretrained, neural network to generate data structures known as vector embeddings. We will compare the solutions of :
- Using [SqueezeNet](https://arxiv.org/abs/1602.07360) to embed images and using Pinecone's vector database offering to find images with similar vector embeddings to a query image from AWS S3.
- Using [CLIP](https://openai.com/research/clip) to embed images and use cosine similarity to find most similar images and load images from AWS S3.


The results shows although CLIP is a much larger and updated model(2021), the SqueezeNet(2016) shows excellent performance in finding similar images and much faster in calculating embeddings.

## Dataset
The dataset we are using is [DeepFashion2](https://github.com/switchablenorms/DeepFashion2), which is a comprehensive fashion dataset. It contains 491K diverse images of 13 popular clothing categories from both commercial shopping stores and consumers. It totally has 801K clothing clothing items, where each item in an image is labeled with scale, occlusion, zoom-in, viewpoint, category, style, bounding box, dense landmarks and per-pixel mask.There are also 873K Commercial-Consumer clothes pairs.
The dataset is split into a training set (391K images), a validation set (34k images), and a test set (67k images).
Examples of DeepFashion2 are shown in Figure 1.

![image](https://user-images.githubusercontent.com/64514218/229259196-707ba69b-a5d0-4de5-b6a3-8f5953809cae.png)
<p align='center'>Figure 1: Clothes sample from data source.</p>

## Workflow

## Visual Search web page showcase
![image](https://user-images.githubusercontent.com/64514218/229259277-e66a723f-2ceb-4586-b392-1f352f7eea5b.png)
![image](https://user-images.githubusercontent.com/64514218/229259289-80deae29-cd8e-4e2c-8864-00d999803554.png)

## Clothes edits with DALL·E 2
The AI empowered app also enable image edits by natural languages, which is amazing.
![image](https://user-images.githubusercontent.com/64514218/229259361-19241d76-970f-49d9-8604-70b9e5ef543d.png)
