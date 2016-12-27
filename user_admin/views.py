from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import Profile

# Create your views here.
def listing_view(request):
    context_dict = {}
    users = Profile.objects.all()
    context_dict['users'] = users
    return render(request, 'listing.html', context_dict)

def edit(request, user_id):
    context_dict = {}
    user_profile = Profile.objects.get(id=user_id)
    context_dict['user_profile'] = user_profile

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        user_location = request.POST.get('user_location')

        if not dob:
            dob = None

        print(user_location)

        user_profile.user.first_name = first_name
        user_profile.user.last_name = last_name
        user_profile.user.email = email
        user_profile.user.save()
        user_profile.mobile = mobile
        user_profile.age = age
        user_profile.dob = dob
        user_profile.user_location = user_location
        user_profile.save()
        return HttpResponse('success')

    return render(request, 'edit.html', context_dict)

def add(request):
    context_dict = {}

    context_dict['new_user'] = True

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        user_location = request.POST.get('user_location')

        if not dob:
            dob = None

        user = User.objects.create(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()
        user_profile = Profile.objects.create(
            user=user,
            mobile = mobile,
            age = age,
            dob = dob,
            user_location = user_location,
        )
        user_profile.save()

        return HttpResponse('success')

    return render(request, 'edit.html', context_dict)
