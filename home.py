import streamlit as st  
import tensorflow as tf
from tensorflow.keras import models, layers
import pickle
from PIL import Image
import numpy as np
import subprocess

def app():
    class_names = ['Aloevera', 'Amla', 'Amruta_Balli', 'Arali', 'Ashoka', 'Ashwagandha', 'Avacado', 'Bamboo', 'Basale', 'Betel', 'Betel_Nut',
              'Brahmi', 'Castor', 'Curry_Leaf', 'Doddapatre', 'Ekka', 'Ganike', 'Gauva', 'Geranium', 'Henna', 'Hibiscus', 'Honge', 'Insulin', 'Jasmine',
              'Lemon', 'Lemon_grass', 'Mango', 'Mint', 'Nagadali', 'Neem', 'Nithyapushpa', 'Nooni', 'Pappaya', 'Pepper', 'Pomegranate', 'Raktachandini', 'Rose',
              'Sapota', 'Tulasi', 'Wood_sorel']
    def preprocess_image(image):
        image = image.resize((128, 128))
    # Convert the image to numpy array
        img_array = np.array(image)
    # Normalize the pixel values
        img_array = img_array / 255.0
        return img_array

    def predict(loaded_model, image):
    # Preprocess the image
        img_array = preprocess_image(image)
        img_array = np.expand_dims(img_array, axis=0)

    # Make predictions
        predictions = loaded_model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = round(100 * np.max(predictions[0]), 2)
        return predicted_class, confidence

    st.subheader("Welcome to Ayurvedic Plant Detection via Image processing")
    st.title(' Image Detection  WebApp')

    st.write('This website is designed for Identification of Different Medicinal Plants/Raw materials through Image Processing Using Machine Learning Algorithm')
    
    if st.button('Detect Now'):
        st.title('AyurVedic Plant detection')
        st.write('Upload an image for classification')

    loaded_model = tf.keras.models.load_model('my_model.keras',compile=False)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button('PREDICT'):
            predicted_class, confidence = predict(loaded_model, image)
            st.write(f'Predicted Class: {predicted_class}')
            st.write(f'Confidence: {confidence}%')


