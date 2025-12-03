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
path('lab9/task6/', views.task6, name='task6'),
path('lab10/listbooks/', views.listbooks, name='listbooks'),
path('lab10/addbook/', views.addbook, name='addbook'),
path('lab10/editbook/<int:id>', views.editbook, name='editbook'),
path('lab10/deletebook/<int:id>', views.deletebook, name='deletebook'),
path('lab10p2/listbooks/', views.listbooks, name='listbooks'),
path('lab10p2/addbook/', views.addbook, name='addbook'),
path('lab10p2/editbook/<int:id>', views.editbook, name='editbook'),
path('lab10p2/deletebook/<int:id>', views.deletebook, name='deletebook'),
path('lab11/students/', views.list_students, name='lab11_liststudents'),
path('lab11/addstudent/', views.add_student, name='lab11_addstudent'),
path('lab11/editstudent/<int:id>/', views.edit_student, name='lab11_editstudent'),
path('lab11/deletestudent/<int:id>/', views.delete_student, name='lab11_deletestudent'),
path('lab11/task2/students/', views.list_students2, name='list_students2'),
path('lab11/task2/addstudent/', views.add_student2, name='add_student2'),
path('lab11/task2/editstudent/<int:id>/', views.edit_student2, name='edit_student2'),
path('lab11/task2/deletestudent/<int:id>/', views.delete_student2, name='delete_student2'),
path('lab11/task3/gallery/', views.gallery_list, name='gallery_list'),
path('lab11/task3/add/', views.add_image, name='gallery_add'),
path('lab11/task3/delete/<int:id>/', views.delete_image, name='gallery_delete'),




]
