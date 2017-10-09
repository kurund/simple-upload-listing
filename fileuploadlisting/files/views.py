from django.shortcuts import render
from django.http import HttpResponse
from .models import File


# Create your views here.
def index(request):
    return HttpResponse("Hello, world! You are at the files index.")


def index(request):
    file_list = File.objects.all()
    print(file_list)
    context = {'file_list': file_list}
    return render(request, 'files/index.html', context)
