from django.shortcuts import render


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
def search_books(request):
    if request.method == "POST":
        keyword = request.POST.get("keyword")
        option1 = request.POST.get("option1")
        option2 = request.POST.get("option2")
        print(keyword, option1, option2)
    return render(request, 'layouts/search.html')


