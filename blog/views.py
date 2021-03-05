from django.shortcuts import render
from .models import Entry,Article

# Create your views here.
def home_view(request):

    return render(request,"home.html",{})


def article_view(request,pk):
    article = Article.objects.get(id=pk)
    entries = article.entry_set.all().order_by("date_added")

    context = {"article": article, "entries": entries} 
    return render(request, "article.html", context)





def articles_view(request):
    articles = Article.objects.all()

    return render(request, "articles.html", {"articles":articles})
