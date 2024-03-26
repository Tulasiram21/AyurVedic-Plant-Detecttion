import streamlit as st  
import tensorflow as tf
from tensorflow.keras import models, layers
import pickle
from PIL import Image
import numpy as np
import subprocess

def app():
    st.subheader("Welcome to Ayurvedic Plant Detection via Image processing")
    st.title(' Image Detection  WebApp')

    st.write('This website is designed for Identification of Different Medicinal Plants/Raw materials through Image Processing Using Machine Learning Algorithm')

    if st.button('Detect Now'):
        subprocess.run(['streamlit', 'run', 'predict.app()'])
    


