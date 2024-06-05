from django.shortcuts import render, redirect

from . import models
from .models import Category
from .forms import CategoryForm
from .models import Market, Review


def index(request):
    categories = Category.objects.all()
    return render(request, 'mainfarmersMarkets/index.html', {'title': 'Главная страница сайта', 'categories': categories})


def about(request):
    return render(request, 'mainfarmersMarkets/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = CategoryForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainfarmersMarkets/create.html', context)


def market_list(request):
    markets = Market.objects.all()
    context = {
        'markets': markets
    }
    return render(request, 'market_list.html', context)


def market_detail(request, market_id):
    market = Market.objects.get(id=market_id)
    reviews = Review.objects.filter(market=market)
    avg_rating = reviews.aggregate(models.Avg('score'))['score__avg']
    context = {
        'market': market,
        'reviews': reviews,
        'avg_rating': avg_rating
    }
    return render(request, 'market_detail.html', context)