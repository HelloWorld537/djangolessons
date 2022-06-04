from django.shortcuts import render
from .models import Order
from .forms import  OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable

# Create your views here.

def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get()
    price_table = PriceTable.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'slider_list': slider_list, 'pc_1': pc_1,
        'price_table': PriceTable, 'form': form, }) 


def success(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name = name, order_phone = phone)
    element.save()
    return render(request, './thanks.html', {'name': name, 'phone': phone})  