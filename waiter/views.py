from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from waiter.models import Food, Order
from django.contrib.auth.decorators import login_required
from .forms import FoodForm, OrderForm


def food_list(request,restaurant='Kempinski'):

    foods =  Food.objects.all()
    nfoods=[]
    # for i in foods:
    #     if i.restaurant &&:
    #         nfoods.append(i)
    foods=[i for i in foods if i.restaurant and i.restaurant.name==restaurant]

    return render(request, 'menu.html',{"foods":foods})
    # return render(request, 'restaurants/Kempinski/kmenu.html',{"foods":foods})

# def order(request):
#     orders =  Order.objects.all()
#     return render(request, 'order.html',{"orders":orders})

def order_list(request):
    form_class = OrderForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
         if form.is_valid():
            customer_name = request.POST.get('customer_name')
            food_name = request.POST.get('food_name')
            table_number = request.POST.get('table_number')
            quantity = request.POST.get('quantity')
            mode = request.POST.get('mode')

            return HttpResponseRedirect('https://rave.flutterwave.com/pay/ghostwaiters3ywm')
    return render(request, 'order.html', {'form': form})
    #     form = OrderForm(request.POST)
    # if form. is_valid():
    #     order = form.save(commit=False)
    #     order.name = customer_name
    #     order.food = food_name
    #     order.number = table_number
    #     order.quantity = quantity
    #     order.save()
    #     return redirect('home')
    # else:
    #     form = OrderForm()
    #
    # return render(request, 'order.html', {'order_form': form})
# def choose_restaurant(request,food_id,town_id):
#     rests = Restaurant.objects.filter(food__id=food_id,
#                                       town__id=town_id)
#     return render(request,'restaurants/choose_restaurant.html',
#                  {'rests':rests})

def restaurant(request, rest_id, message=''):
    rest = Restaurant.objects.get(id=rest_id)
    rest_menu = rest.menu.split(';')
    rest_menu = [e for e in rest_menu if e not in ('',' ')]
    return render(request, 'restaurants/restaurant.html',
                 {'restaurant':rest, 'rest_menu': rest_menu,
                  'message':message})

def vote(request, rest_id):
    rest = get_object_or_404(Restaurant, pk=rest_id)

    votes = rest.votes
    submitted = request.POST['note_utilisateur']
    average = (votes + int(submitted))/2
    rest.votes = average
    rest.save()

    rest_menu = rest.menu.split(';')
    rest_menu = [e for e in rest_menu if e not in ('',' ')]

    message='Thanks for your vote!'
    return render(request, 'restaurants/restaurant.html',
                 {'restaurant':rest, 'rest_menu': rest_menu,
                  'message':message})


@login_required(login_url="/accounts/login/")
def profile(request):
    return render_to_response('registration/login.html',
                              context_instance=RequestContext(request))
