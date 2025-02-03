import numpy as np
import streamlit as st
import eda
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow_hub.keras_layer import KerasLayer
import tensorflow as tf
from tensorflow.keras.models import load_model


def run():
    st.image('https://images.tokopedia.net/img/cache/850/BgtCLw/2024/7/30/b8921d78-0471-4b45-9a1a-ea554e1f67e9.jpg?ect=4g')
    st.title("Shoes Classification Model")


    # File uploader widget for users to upload an image
    file = st.file_uploader("Upload an image", type=["jpg", "png"])

    # Load the pre-trained model
    model = load_model('model.keras', custom_objects={'KerasLayer': KerasLayer})
    
    # Set the target size to which images should be resized
    target_size = (128, 128)

    # Define the class mapping
    class_mapping = {'adidas': 0, 'converse': 1, 'nike': 2}

    # Function to preprocess the image and make predictions
    def import_and_predict(image_data, model):
        # Load the image and resize it to the target size
        image = load_img(image_data, target_size=(128, 128))
        img_array = img_to_array(image)
        
        # Expand dimensions to match the input shape (batch size, width, height, channels)
        img_array = tf.expand_dims(img_array, 0)  # Create a batch

        # Normalize the image by scaling pixel values to [0, 1]
        img_array = img_array / 255.0

        # Make the prediction using the model
        predictions = model.predict(img_array)

        # Get the predicted class index (0, 1, or 2)
        predicted_index = np.argmax(predictions)

        # Reverse the class mapping to get the class name from the index
        predicted_class = [key for key, value in class_mapping.items() if value == predicted_index][0]

        # Return the predicted class name
        result = f"Prediction: {predicted_class}"

        return result

    # Check if the user uploaded a file
    if file is None:
        st.text("Please upload an image file")
    else:
        # Process the image and make the prediction
        result = import_and_predict(file, model)
        
        # Display the uploaded image
        st.image(file)
        
        # Display the result of the prediction
        st.write(result)

        
# Run the Streamlit app
if __name__ == "__main__":
    run()
