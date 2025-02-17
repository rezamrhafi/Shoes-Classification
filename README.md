# Shoes Classification - ![Deep Learning](https://img.shields.io/badge/Deep%20Learning-FF6F20?style=for-the-badge&logo=TensorFlow&logoColor=white)

This repository contains a project for shoe brand segmentation using Deep Learning and Computer Vision techniques. The goal of this project is to analyze the shape of shoes and categorize the corresponding brand based on that analysis. This repository includes Jupyter Notebook files that explain the entire process, from data exploration to deep learning model implementation.

---

## Related Project Links ⛓️‍💥

- [Dataset](https://www.kaggle.com/datasets/die9origephit/nike-adidas-and-converse-imaged)
- [Deployment](https://huggingface.co/spaces/RezaMRhafi/GC7)

---

## Project Overview 📝

In this project, I use Deep Learning techniques to analyze the shape of shoes and classify them into their respective brands. Some key steps covered in this project include:

1. **Import Libraries and Data Exploration**:
    - Loading the dataset and performing initial exploration to understand the structure and characteristics of the data.

2. **Data Preprocessing**:
    - Cleaning and preparing the data, including image handling and normalization.

3. **Training Base Model**:
    - Building and training a deep learning model to identify shoe shapes.

4. **Base Model Evaluation**:
    - Using evaluation metrics to assess the model's performance.

5. **Model Tuning**:
    - Building and training a deep learning model with hyperparameter tuning to identify shoe shapes more effectively.

6. **Tuned Model Evaluation**:
    - Using evaluation metrics to assess the performance of the tuned model.

7. **Decision Making**:
    - Making decisions based on the model's performance.

---

## Problem Background 🧐

In the retail industry, the process of receiving goods in a warehouse is a crucial stage in supply chain management. Mistakes in product identification, especially shoes from brands such as Converse, Nike, and Adidas, can lead to inaccuracies in stock recording, distribution, and customer service. Therefore, an automated system capable of recognizing shoe brands from product images is needed to improve efficiency and accuracy in warehouse operations.

To address this issue, an AI-based classification model was developed to automatically identify shoe brands from images of products received in the warehouse. This model is built using machine learning with TensorFlow and tested with two approaches: without data augmentation and with data augmentation. Data augmentation is used to increase the variation in the dataset, making the model more robust to different lighting conditions, angles, and backgrounds.

The best-performing model, the one with data augmentation, will be used for deployment to ensure optimal accuracy in real-world warehouse conditions. The implementation of this model is expected to speed up product identification, reduce human errors, and improve operational efficiency.

---

## Methods Used 🛠️

- Deep Learning
- Computer Vision
- Image Classification
- Data Visualization

---

## Conclusion 💡

- After inference testing, the model still frequently struggles to differentiate between Adidas and Nike shoes. Converse shoes are easier for the model to recognize.
- Of the three optimizers tested, Adamax was the most optimal for this dataset compared to Adam and Nadam.
- The model performs poorly when data augmentation parameters are too extreme, as it becomes difficult for the model to distinguish between classes.
- Using too many layers in the model can decrease accuracy in class predictions.
- If the number of epochs is too high, the model may become overfitted.
- Without augmentation, the model tends to overfit significantly.
