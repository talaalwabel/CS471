from .models import Book, Publisher, Author
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Book, Address, Student, Student2, Address2, Gallery
from datetime import datetime
from .forms import GalleryForm


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

def task3(request):
    publishers = Publisher.objects.annotate(
        oldest_book_date=Min('book__pubdate')
    )

    return render(request, 'bookmodule/lab9/task3.html', {'publishers': publishers})

def task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9/task4.html', {'publishers': publishers})

def task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9/task5.html', {'publishers': publishers})


def task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count(
            'book',
            filter=Q(book__price__gt=50, book__quantity__lt=5, book__quantity__gte=1)
        )
    )

    return render(request, 'bookmodule/lab9/task6.html', {'publishers': publishers})


def listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10/listbooks.html', {'books': books})



def addbook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        publisher_id = request.POST.get('publisher')

        
        publisher = Publisher.objects.get(id=publisher_id)

        
        Book.objects.create(
            title=title,
            price=price,
            quantity=quantity,
            pubdate=datetime.now(),
            publisher=publisher
        )

        return redirect('/books/lab10/listbooks')

    
    publishers = Publisher.objects.all()
    return render(request, 'bookmodule/lab10/addbook.html', {'publishers': publishers})



def editbook(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        publisher_id = request.POST.get('publisher')
        book.publisher = Publisher.objects.get(id=publisher_id)
        book.pubdate = datetime.now()

        book.save()

        return redirect('/books/lab10/listbooks')

    publishers = Publisher.objects.all()
    return render(request, 'bookmodule/lab10/editbook.html', {
        'book': book,
        'publishers': publishers
    })


def deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/books/lab10/listbooks')

def listbooks_p2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10p2/listbooks.html', {'books': books})

def addbook_p2(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.pubdate = datetime.now()
            book.save()
            return redirect('/books/lab10p2/listbooks')
    else:
        form = BookForm()

    return render(request, 'bookmodule/lab10p2/addbook.html', {'form': form})
def editbook_p2(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/lab10p2/listbooks')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodule/lab10p2/editbook.html', {'form': form})

def deletebook_p2(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books/lab10p2/listbooks')

def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab11/list_students.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        address_id = request.POST.get('address')

        address = Address.objects.get(id=address_id)

        Student.objects.create(
            name=name,
            age=age,
            address=address
        )

        return redirect('/books/lab11/students/')

    addresses = Address.objects.all()
    return render(request, 'bookmodule/lab11/add_student.html', {'addresses': addresses})

def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        address_id = request.POST.get('address')
        student.address = Address.objects.get(id=address_id)

        student.save()
        return redirect('/books/lab11/students/')

    addresses = Address.objects.all()
    
    return render(request, 'bookmodule/lab11/edit_student.html', {
        'student': student,
        'addresses': addresses
    })

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/books/lab11/students/')

def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/lab11/task2/list_students2.html', {'students': students})

def add_student2(request):
    addresses = Address2.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        selected_addresses = request.POST.getlist('addresses')

        student = Student2.objects.create(name=name, age=age)
        student.addresses.set(selected_addresses)

        return redirect('/books/lab11/task2/students/')

    return render(request, 'bookmodule/lab11/task2/add_student2.html', {'addresses': addresses})

def edit_student2(request, id):
    student = Student2.objects.get(id=id)
    addresses = Address2.objects.all()

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        selected_addresses = request.POST.getlist('addresses')

        student.addresses.set(selected_addresses)
        student.save()

        return redirect('/books/lab11/task2/students/')

    return render(request, 'bookmodule/lab11/task2/edit_student2.html', {
        'student': student,
        'addresses': addresses
    })

def delete_student2(request, id):
    student = Student2.objects.get(id=id)
    student.delete()
    return redirect('/books/lab11/task2/students/')

def gallery_list(request):
    images = Gallery.objects.all()
    return render(request, 'bookmodule/lab11/task3/gallery_list.html', {'images': images})


def add_image(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/books/lab11/task3/gallery/')
    else:
        form = GalleryForm()

    return render(request, 'bookmodule/lab11/task3/add_image.html', {'form': form})


def delete_image(request, id):
    img = Gallery.objects.get(id=id)
    img.delete()
    return redirect('/books/lab11/task3/gallery/')