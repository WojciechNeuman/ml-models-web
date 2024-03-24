from django.shortcuts import render
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


vect = CountVectorizer()

model = load('./savedModels/firstModel.joblib')
vectorizer = load('./savedModels/vectorizer.joblib')

print(type(vectorizer))

def predictor(request):
    return render(request, 'predictor.html')

def autextification_page(request):
    return render(request, 'autextification.html')

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