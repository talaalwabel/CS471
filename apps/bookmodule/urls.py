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
path('html5/tables/', views.html5_tables, name='html5_tables'),
path('search/', views.search_books, name='search_books'),
path('simple/query/', views.simple_query, name='simple_query'),
path('complex/query/', views.lookup_query, name='lookup_query'),
path('lab9/task1/', views.task1, name='task1'),
path('lab9/task2/', views.task2, name='task2'),
path('lab9/task3/', views.task3, name='task3'),
path('lab9/task4/', views.task4, name='task4'),
path('lab9/task5/', views.task5, name='task5'),



]
