from django.shortcuts import render
from .models import Category,Post
# Create your views here.
def home(request):
    homes = Post.objects.all()
    print(homes)
    return render(request,'index.html',{'homes':homes})





