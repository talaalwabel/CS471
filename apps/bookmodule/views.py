from django.shortcuts import render




def index(request): 
name = request.GET.get("name") or "world!" 
return render(request, "bookmodule/index.html" , {"name": name})  #your render line 


def index2(request, val1=0):
    return render(request, "bookmodule/index.html", {"name": f"value1 = {val1}"})