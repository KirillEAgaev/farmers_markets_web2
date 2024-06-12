from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
from django.views.generic import ListView
from math import radians, sin, cos, sqrt, atan2

from .models import Categories, Cities, States
from .forms import CategoryForm
from .models import Markets, Reviews


def index(request):
    category = Categories.objects.all()
    return render(request, 'mainfarmersMarkets/index.html', {'title': 'Главная страница сайта', 'category': category})


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


class MarketListView(ListView):
    model = Markets
    template_name = 'market_list.html'  # Шаблон для отображения списка рынков
    context_object_name = 'markets'      # Имя переменной, которая будет использоваться в шаблоне

    paginate_by = 20  # Разбивка на страницы, по 20 элементов на страницу

    def get_queryset(self):
        return Markets.objects.all()  # Возвращает список всех объектов Market

def market_detail(request, id):
    market = get_object_or_404(Markets, market_id=id)
    reviews = Reviews.objects.filter(market=market)
    avg_rating = reviews.aggregate(Avg('score'))['score__avg']
    context = {
        'market': market,
        'reviews': reviews,
        'avg_rating': avg_rating
    }
    return render(request, 'market_detail.html', context)


def calculate_distance(lat1, lon1, lat2, lon2):
    # Конвертируем координаты из градусов в радианы
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Радиус Земли в километрах
    R = 6371.0

    # Разница широт и долгот
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c  # Расстояние в километрах

    return distance

def search_market(request):
    if request.method == 'GET':
        city_name = request.GET.get('city')
        state_abbr = request.GET.get('state')
        postal_code = request.GET.get('postal_code')
        max_distance = float(request.GET.get('max_distance', 30))  # По умолчанию 30 километров

        try:
            city = Cities.objects.get(city=city_name)
        except Cities.DoesNotExist:
            city = None

        try:
            state = States.objects.get(state_abbr=state_abbr)
        except States.DoesNotExist:
            state = None

        if city and state:
            markets = Markets.objects.filter(city=city, state=state, zip=postal_code)

            if max_distance:
                filtered_markets = []
                for market in markets:
                    market_coords = (market.lat, market.lon)
                    search_coords = (city.lat, city.lon)  # Координаты города для поиска по дальности

                    distance = calculate_distance(market_coords[0], market_coords[1], search_coords[0], search_coords[1])
                    if distance <= max_distance:
                        filtered_markets.append(market)

                markets = filtered_markets

            context = {
                'markets': markets
            }
            return render(request, 'market_list.html', context)
        else:
            error_message = "Invalid city or state provided."
            context = {
                'error_message': error_message
            }
        return render(request, 'market_list.html', context)