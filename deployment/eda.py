import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def run():
    st.title('Shoes Classifier Exploratory Data Analysis')
    st.write('## Data yang akan diprediksi')
    st.write('Adidas')
    st.image('https://i.ibb.co.com/5rwZMnL/train-adidas.png')
    st.write('Converse')
    st.image('https://i.ibb.co.com/9s3vSR6/converse.png')
    st.write('Nike')
    st.image('https://i.ibb.co.com/VS0XvPQ/nike.png')



    st.write('## Jumlah data Train')
    st.write('1. Adidas : 237')
    st.write('2. Converse : 237')
    st.write('3. Nike : 237')

    st.write('## Jumlah data Test')
    st.write('1. Adidas : 38')
    st.write('2. Converse : 38')
    st.write('3. Nike : 38')


    st.write('## Model Evaluation')
    st.image('https://i.ibb.co.com/K6jnCHf/metrics.png')
    st.write('berdasarkan gambar dari plot, nilai epoch yang optimal berada pada 36 hingga 40 dikarenakan pada sekitar epoch tersebut goodfit')


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def run():
    st.title('Shoes Classifier Exploratory Data Analysis')
    
    st.write('## Data yang akan diprediksi')
    st.write('Adidas')
    st.image('adidas.png')
    st.write('Converse')
    st.image('converse.png')
    st.write('Nike')
    st.image('nike.png')

    st.write('## Jumlah data Train')
    st.write('1. Adidas : 237')
    st.write('2. Converse : 237')
    st.write('3. Nike : 237')

    st.write('## Jumlah data Test')
    st.write('1. Adidas : 38')
    st.write('2. Converse : 38')
    st.write('3. Nike : 38')

if __name__ == '__main__':
    run()