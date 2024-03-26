from django.shortcuts import render
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from PIL import Image
import io
import os


vect = CountVectorizer()

model = load('./savedModels/firstModel.joblib')
vectorizer = load('./savedModels/vectorizer.joblib')
model_digit = load('./savedModels/sgd_digits.joblib')

print(type(vectorizer))

def predictor(request):
    return render(request, 'predictor.html')

def autextification_page(request):
    return render(request, 'autextification.html')

def digit_recognizer_page(request):
    return render(request, 'digit_recognizer.html')

def autextification_result(request):
    text = request.GET['text_in_english']
    # need stop engine wait stops would Check safe

    x_test = pd.Series([text])

    y_pred = vectorizer.transform(x_test)

    print(y_pred)

    y_pred = model.predict(y_pred)

    if y_pred[0] == 0:
        y_pred = 'Human'
    else:
        y_pred = 'Computer'

    return render(request, 'autextification_result.html', {'result': y_pred})

def digit_recognizer_result(request):

    if request.method == 'POST':
        # Check if the form was submitted using POST method
        if 'image' in request.FILES:
            # Get the uploaded file from request.FILES
            uploaded_image = request.FILES['image']
            print(f"Type: {type(uploaded_image)}")
            # Perform further processing with the uploaded image
            pil_image = Image.open(uploaded_image)
            
            # Convert the image to grayscale
            grayscale_image = pil_image.convert('L')

            # Resize the image to 28x28 pixels
            resized_image = grayscale_image.resize((28, 28))

            # Convert the image to black and white
            threshold = 100  # Adjust the threshold as needed
            bw_image = resized_image.point(lambda x: 0 if x < threshold else 255, '1')

            # Save the black and white image
            current_directory = os.getcwd()
            image_path = os.path.join(current_directory, 'bw_image.jpg')
            bw_image.save(image_path, format='JPEG')  # Change the format as needed
        else:
            # Handle the case where 'image' key is not found in request.FILES
            print("No image file uploaded")
    else:
        # Handle the case where the form was not submitted using POST method
        print("Form not submitted using POST method")
    # text = request.GET['text_in_english']
    # # need stop engine wait stops would Check safe

    # x_test = pd.Series([text])

    # y_pred = vectorizer.transform(x_test)

    # print(y_pred)

    # y_pred = model.predict(y_pred)

    # if y_pred[0] == 0:
    #     y_pred = 'Human'
    # else:
    #     y_pred = 'Computer'

    y_pred = 1

    return render(request, 'digit_recognizer_result.html', {'result': y_pred})


def image_to_dataframe(image):
    # Convert the PIL Image object to a list of pixel values
    pixel_values = list(image.getdata())

    # Create a DataFrame with one row and 784 columns (28x28 pixels)
    df = pd.DataFrame([pixel_values], columns=[f'pixel{i+1}' for i in range(784)])

    # Scale the pixel values from 0 to 255 to a range from 0.0 to 1.0
    df = df / 255.0

    return df