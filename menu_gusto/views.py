from django.shortcuts import render
from main_gusto.models import Dish
from main_gusto.forms import CategoryAddForm
# Create your views here.


def dish_info(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'dish.html', context={
        'dish': dish,
    }
                  )


def category_add(request):
    form1 = CategoryAddForm()
    return render(request, 'categoryadd.html', context={
        'form1': form1
    })
