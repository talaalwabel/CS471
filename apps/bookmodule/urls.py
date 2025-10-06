from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [ 
path('', views.index, name= "books.index"), 
path('list_books/', views.list_books, name= "books.list_books"), 
path('<int:bookId>/', views.viewbook, name="books.one_book"), 
path('aboutus/', views.aboutus, name="books.aboutus"), 
path('html5/links/', views.html5_links, name='html5_links'),
path('html5/text/formatting/', views.text_formatting, name='text_formatting'),
path('html5/listing/', views.html5_listing, name='html5_listing'),

]
