from django.shortcuts import render, redirect
from .models import Category, Dish, Event, Banners
import datetime
from .forms import UserMessageForm, CategoryAddForm, DishAddForm


def main(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        form1 = CategoryAddForm(request.POST)
        form2 = DishAddForm(request.POST)
        if form.is_valid():
            form.save()
        if form1.is_valid():
            form1.save()
        if form2.is_valid():
            form2.save()
        return redirect('/')

    special_categories = Category.objects.filter(is_visible=True).filter(is_special=True).order_by('category_order')
    for item in special_categories:
        item.dishes = Dish.objects.filter(category=item.pk)

    categories = Category.objects.filter(is_visible=True).filter(is_special=False).order_by('category_order')
    for item in categories:
        item.dishes = Dish.objects.filter(category=item.pk)

    events = Event.objects.filter(event_date__gte=datetime.date.today())

    banners = Banners.objects.filter(is_visible=True)

    users_messages_form = UserMessageForm()

    add_category_form = CategoryAddForm()

    add_dish_form = DishAddForm()
    return render(request, 'index.html', context={'categories': categories,
                                                  'special_categories': special_categories,
                                                  'events': events,
                                                  'banners': banners,
                                                  'form': users_messages_form,
                                                  'form1': add_category_form,
                                                  'form2': add_dish_form,
                                                  }
                  )
