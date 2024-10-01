from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('-date')  # Get all articles
    paginator = Paginator(articles, 5)  # Show 5 articles per page

    page_number = request.GET.get('page')  # Get the page number from the URL
    articles = paginator.get_page(page_number)  # Get the articles for the current page

    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
