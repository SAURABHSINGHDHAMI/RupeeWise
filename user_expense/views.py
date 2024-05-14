from django.shortcuts import render, redirect, get_object_or_404
from .forms import BillForm, ClothForm, FoodForm, TravelForm, SubscriptionForm, MiscellaneousForm
from .models import Bill, Cloth, Food, Travel, Subscription, Miscellaneous
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def dashboard(request):

    user = request.user

    user_bill_form = BillForm()
    user_cloth_form = ClothForm()
    user_food_form = FoodForm()
    user_travel_form = TravelForm()
    user_subscription_form = SubscriptionForm()
    user_miscellaneous_form = MiscellaneousForm()

    user_bill = Bill.objects.filter(user = request.user)
    user_cloth = Cloth.objects.filter(user = request.user)
    user_food = Food.objects.filter(user = request.user)
    user_travel = Travel.objects.filter(user = request.user)
    user_subscription = Subscription.objects.filter(user = request.user)
    user_miscellaneous = Miscellaneous.objects.filter(user = request.user)

    current_date = datetime.now()

    context = {
        'user_bill_form': user_bill_form,
        'user_cloth_form': user_cloth_form,
        'user_food_form': user_food_form,
        'user_travel_form': user_travel_form,
        'user_subscription_form': user_subscription_form,
        'user_miscellaneous_form': user_miscellaneous_form,

        'user_bill' : user_bill,
        'user_cloth' : user_cloth,
        'user_food' : user_food,
        'user_travel' : user_travel,
        'user_subscription' : user_subscription,
        'user_miscellaneous' : user_miscellaneous,

        'user' : user,

        'current_date' : current_date,
    }

# --------------------bill - save | delete--------------------

    if request.method == 'POST':
        if "save_bill" in request.POST:
            user_bill_form = BillForm(request.POST)
            if user_bill_form.is_valid():
                bill = user_bill_form.save(commit=False)
                bill.user = request.user
                bill.save()
                return redirect('dashboard')
        elif "delete_bill" in request.POST:
            pk = request.POST.get("delete_bill")
            delete_user_bill = Bill.objects.get(id = pk)
            delete_user_bill.delete()
            return redirect('dashboard')

# --------------------cloth - save | delete--------------------
        
        elif "save_cloth" in request.POST:
            user_cloth_form = ClothForm(request.POST)
            if user_cloth_form.is_valid():
                cloth = user_cloth_form.save(commit=False)
                cloth.user = request.user
                cloth.save()
                return redirect('dashboard')
        elif "delete_cloth" in request.POST:
            pk = request.POST.get("delete_cloth")
            delete_cloth_bill = Cloth.objects.get(id = pk)
            delete_cloth_bill.delete()
            return redirect('dashboard')

# --------------------food - save | delete-------------------- 

        elif "save_food" in request.POST:
            user_food_form = FoodForm(request.POST)
            if user_food_form.is_valid():
                food = user_food_form.save(commit=False)
                food.user = request.user
                food.save()
                return redirect('dashboard')
        elif "delete_food" in request.POST:
            pk = request.POST.get("delete_food")
            delete_food_bill = Food.objects.get(id = pk)
            delete_food_bill.delete()
            return redirect('dashboard')
        
# --------------------travel - save | delete--------------------

        elif "save_travel" in request.POST:
            user_travel_form = TravelForm(request.POST)
            if user_travel_form.is_valid():
                travel = user_travel_form.save(commit=False)
                travel.user = request.user
                travel.save()
                return redirect('dashboard')
        elif "delete_travel" in request.POST:
            pk = request.POST.get("delete_travel")
            delete_travel_bill = Travel.objects.get(id = pk)
            delete_travel_bill.delete()
            return redirect('dashboard')
        
# --------------------subscription - save | delete--------------------

        elif "save_subscription" in request.POST:
            user_subscription_form = SubscriptionForm(request.POST)
            if user_subscription_form.is_valid():
                subscription = user_subscription_form.save(commit=False)
                subscription.user = request.user
                subscription.save()
                return redirect('dashboard')
        elif "delete_subscription" in request.POST:
            pk = request.POST.get("delete_subscription")
            delete_subscription_bill = Subscription.objects.get(id = pk)
            delete_subscription_bill.delete()
            return redirect('dashboard')
        
# --------------------miscellaneous - save | delete--------------------

        elif "save_miscellaneous" in request.POST:
            user_miscellaneous_form = MiscellaneousForm(request.POST)
            if user_miscellaneous_form.is_valid():
                miscellaneous = user_miscellaneous_form.save(commit=False)
                miscellaneous.user = request.user
                miscellaneous.save()
                return redirect('dashboard')
        elif "delete_miscellaneous" in request.POST:
            pk = request.POST.get("delete_miscellaneous")
            delete_miscellaneous_bill = Miscellaneous.objects.get(id = pk)
            delete_miscellaneous_bill.delete()
            return redirect('dashboard')

    return render(request, 'user_expense/dashboard.html', context)
