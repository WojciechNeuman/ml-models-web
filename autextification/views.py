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
            
            pil_image = Image.open(uploaded_image)

            grayscale_image = pil_image.convert('L')

            final_image = grayscale_image.resize((28, 28))


            df_image = image_to_dataframe(final_image)

            y_pred = model_digit.predict(df_image)[0]

        else:
            # Handle the case where 'image' key is not found in request.FILES
            print("No image file uploaded")
    else:
        # Handle the case where the form was not submitted using POST method
        print("Form not submitted using POST method")


    return render(request, 'digit_recognizer_result.html', {'result': y_pred})


def image_to_dataframe(image):
    # convert image to list of pixels
    pixel_values = list(image.getdata())

    # Dataframe with column names corresponding to the column names of a model
    df = pd.DataFrame([pixel_values], columns=[f'pixel{i+1}' for i in range(784)]) 

    
    # switch white images with black numbers to black with white numbers
    if df.values.mean() > 100:
        df = 255.0 - df

    return df