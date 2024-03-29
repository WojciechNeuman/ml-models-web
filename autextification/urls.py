from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor, name = 'predictor'),
    path('about', views.about, name = 'about_section'),
    path('autextification/', views.autextification_page, name='autextification_page'),
    path('digit-recognizer/', views.digit_recognizer_page, name='digit_recognizer_page'),
    
]