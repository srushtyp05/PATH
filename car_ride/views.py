from .models import Ride
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RideForm
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'car_ride/home.html')

def all_rides(request):
    rides = Ride.objects.all()
    return render(request, 'car_ride/all_rides.html', {'rides':rides})

def post_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_rides')
    else:
        form = RideForm()
    return render(request, 'car_ride/post_ride.html', {'form': form})

def edit_ride(request, ride_id):
    ride = get_object_or_404(Ride, pk=ride_id)
    if request.method == 'POST':
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            form.save()
            return redirect('all_rides')
    else:
        form = RideForm(instance=ride)
    return render(request, 'car_ride/edit_ride.html', {'form': form})

def about_us(request):
    return render(request, 'car_ride/about_us.html')

def landing(request):
    return render(request, 'landing.html')

def passenger_home(request):
    return render(request, 'passenger/passenger_home.html')

def passenger_rides(request):
    rides = Ride.objects.all()
    return render(request, 'passenger/passenger_rides.html', {'rides': rides})