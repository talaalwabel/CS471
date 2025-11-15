from .models import Book, Publisher, Author
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Book, Address, Student  

def index(request): 
    return render(request, "bookmodule/index.html") 
def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html') 
def html5_links(request):
    return render(request, 'bookmodule/html5/links.html')
def text_formatting(request):
    return render(request, 'bookmodule/html5/text/formatting.html')
def html5_listing(request):
    return render(request, 'bookmodule/html5/listing.html')
def html5_tables(request):
    return render(request, 'bookmodule/html5/tables.html')
def __getBooksList(): 
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
    return [book1, book2, book3] 


def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)
        
    
        return render(request, 'layouts/bookList.html', {'books': newBooks})
    
    
    return render(request, 'layouts/search.html')


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')  
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
                          .filter(title__icontains='and')\
                          .filter(edition__gte=2)\
                          .exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=2) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def students_per_city(request):
    data = Student.objects.values('address__city').annotate(num_students=Count('id'))
    return render(request, 'bookmodule/task7.html', {'data': data})




def task1(request):
    total_books = Book.objects.aggregate(total=Sum('quantity'))['total'] or 1
    books = Book.objects.all()
    for book in books:
        book.percentage = round((book.quantity / total_books) * 100, 2)
    return render(request, 'bookmodule/lab9/task1.html', {'books': books})

def task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9/task2.html', {'publishers': publishers})