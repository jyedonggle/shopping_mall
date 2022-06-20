from django.shortcuts import render
from climey.models import Good

# Create your views here.

def index(request):
    goods = Good.objects.all().order_by('pk')

    return render(
        request,
        'climey/index.html',
        {
            'goods' : goods
        }
    )