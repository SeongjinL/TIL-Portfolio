from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'my_board/list.html')

def login(request):
    return render(request, 'my_board/login.html')

def write(request):
    return render(request, 'my_board/write.html')
