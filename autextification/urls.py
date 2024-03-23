from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor, name = 'predictor'),
    path('/main/result', views.formInfo, name = 'result'),
    path('main/', views.main_page, name='main_page'),  # Add this URL pattern

]