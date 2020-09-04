from django.shortcuts import render, get_object_or_404
from PortApp.models import article
# Create your views here.
def HomePage(request):
    Articles = article.objects.all()
    context = {'posts':Articles}
    return render(request,'home.html',context)

def DetailPage(request,postTitle):
    ParArticle = get_object_or_404(article,Title = postTitle)
    context = {'article':ParArticle}
    return render(request,'detail.html',context)