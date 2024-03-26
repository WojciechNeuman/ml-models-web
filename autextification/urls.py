from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor, name = 'predictor'),
    path('autextification/result', views.autextification_result, name = 'result'),
    path('autextification/', views.autextification_page, name='autextification_page'),
    path('digit-recognizer/', views.digit_recognizer_page, name='digit_recognizer_page'),
    path('digit-recognizer/result', views.digit_recognizer_result, name = 'digit_result'),
    
]