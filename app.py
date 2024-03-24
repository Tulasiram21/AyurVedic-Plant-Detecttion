import streamlit as st  
import tensorflow as tf
from tensorflow.keras import models, layers
import pickle
import numpy as np
from PIL import Image


st.set_page_config(page_title="AyurVedic",layout="wide")


class_names = ['Aloevera', 'Amla', 'Amruta_Balli', 'Arali', 'Ashoka', 'Ashwagandha', 'Avacado', 'Bamboo', 'Basale', 'Betel', 'Betel_Nut',
              'Brahmi', 'Castor', 'Curry_Leaf', 'Doddapatre', 'Ekka', 'Ganike', 'Gauva', 'Geranium', 'Henna', 'Hibiscus', 'Honge', 'Insulin', 'Jasmine',
              'Lemon', 'Lemon_grass', 'Mango', 'Mint', 'Nagadali', 'Neem', 'Nithyapushpa', 'Nooni', 'Pappaya', 'Pepper', 'Pomegranate', 'Raktachandini', 'Rose',
              'Sapota', 'Tulasi', 'Wood_sorel']


def preprocess_image(image):
    # Resize the image to the required input size of the model
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

# Main Streamlit app
def main():
    st.title('AyurVedic Plant detection')
    st.write('Upload an image for classification')

    # Load the saved model
    loaded_model = tf.keras.models.load_model('my_model.keras')

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button('PREDICT'):
            predicted_class, confidence = predict(loaded_model, image)
            st.write(f'Predicted Class: {predicted_class}')
            st.write(f'Confidence: {confidence}%')

if __name__ == '__main__':
    main()
