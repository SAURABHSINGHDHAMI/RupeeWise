from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile
from user_expense.models import Bill, Cloth, Food, Travel, Subscription, Miscellaneous
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = None
    
    if user_profile is not None:
        user_profile_form = ProfileForm(instance=user_profile)
    else:
        user_profile_form = ProfileForm()

# --------------------bill--------------------

    user_bill = Bill.objects.filter(user=request.user)

    total_bill_amount = 0

    for bill_amount in user_bill:
        total_bill_amount += bill_amount.amount

# --------------------cloth--------------------

    user_cloth = Cloth.objects.filter(user=request.user)

    total_cloth_amount = 0

    for cloth_amount in user_cloth:
        total_cloth_amount += cloth_amount.amount

# --------------------food--------------------

    user_food = Food.objects.filter(user=request.user)

    total_food_amount = 0

    for food_amount in user_food:
        total_food_amount += food_amount.amount

# --------------------travel--------------------

    user_travel = Travel.objects.filter(user=request.user)

    total_travel_amount = 0

    for travel_amount in user_travel:
        total_travel_amount += travel_amount.amount

# --------------------subscription--------------------

    user_subscription = Subscription.objects.filter(user=request.user)

    total_subscription_amount = 0

    for subscription_amount in user_subscription:
        total_subscription_amount += subscription_amount.amount

# --------------------miscellaneous--------------------

    user_miscellaneous = Miscellaneous.objects.filter(user=request.user)

    total_miscellaneous_amount = 0

    for miscellaneous_amount in user_miscellaneous:
        total_miscellaneous_amount += miscellaneous_amount.amount
        
    context = {
        'user_profile_form': user_profile_form,

        'user_bill': user_bill,
        'total_bill_amount': total_bill_amount,

        'user_cloth': user_cloth,
        'total_cloth_amount': total_cloth_amount,

        'user_food': user_food,
        'total_food_amount': total_food_amount,

        'user_travel': user_travel,
        'total_travel_amount': total_travel_amount,

        'user_subscription': user_subscription,
        'total_subscription_amount': total_subscription_amount,

        'user_miscellaneous': user_miscellaneous,
        'total_miscellaneous_amount': total_miscellaneous_amount,
    }
    return render(request, 'user_profile/profile.html', context)