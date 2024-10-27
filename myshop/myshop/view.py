from django.http import HttpResponse

def hello_paje(request):
    return HttpResponse("<h1>Hello World!</h1>")