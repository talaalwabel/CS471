from django.urls import path 
from . import views 
urlpatterns = [ 
path('', views.index), 
path('index2/<val1>/', views.index2)
] 