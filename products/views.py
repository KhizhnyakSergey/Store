from django.shortcuts import render

# Create your views here.
# контроллеры = views (вьюхи) = функции


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог'
    }
    return render(request, 'products/products.html', context)


def test_context(request):
    context = {
        'title': 'store',
        'header': 'Добро пожаловать!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 600.00},
            {'name': 'Синяя куртка The North Face', 'price': 1800.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 849.00},
        ],
        # 'promotion': True,
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': 500.00},
        ]
    }
    return render(request, 'products/test-context.html', context)
