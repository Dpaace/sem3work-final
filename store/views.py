from django.shortcuts import render
from accounts import models
from django.core.paginator import Paginator
# Create your views here.
def store(request):
    products=models.Product.objects.order_by('-name')
    # products=models.Product.objects.filter(available='In Stock')
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'products': paged_product,
    }
    return render(request, 'store/store.html',data)

# def about(request):
#     return render(request, 'pages/about.html')
