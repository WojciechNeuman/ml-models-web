from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor, name = 'predictor'),
    path('autextification/result', views.autextification_result, name = 'result'),
    path('autextification/', views.autextification_page, name='autextification_page'),
]