# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import FeedbackForm
from .forms import ChildForm
from .forms import BusStopForm
from .models import Child
from .models import PopRegister
from .forms import PopRegisterForm
from .models import Parent, Operator, Bus, BusTrack, Feedback, BusMileage
from .forms import ParentForm, OperatorForm, BusForm, BusMileageForm
from .models import PopRegister, Exclusion
from .forms import ExclusionForm

@login_required
def register_management(request):
    pop_register_data = PopRegister.objects.all()
    return render(request, 'register_management.html', {'pop_register_data': pop_register_data})

@login_required
def exclusion_management(request):
    if request.method == 'POST':
        form = ExclusionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('register_management.html')  # Redirect to register management or another appropriate page
    else:
        form = ExclusionForm()

    exclusions = Exclusion.objects.all()

    return render(request, 'exclusion_management.html', {'form': form, 'exclusions': exclusions})


@login_required
def bus_mileage(request):
    # Assuming you have a form to submit the bus mileage
    if request.method == 'POST':
        form = BusMileageForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = BusMileageForm()

    bus_mileage_entries = BusMileage.objects.all()
    return render(request, 'bus_mileage.html', {'form': form, 'bus_mileage_entries': bus_mileage_entries})

@login_required
def feedback_inbox(request):
    feedback_entries = Feedback.objects.all()
    return render(request, 'feedback_inbox.html', {'feedback_entries': feedback_entries})

@login_required
def add_remove_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin_dashboard.html')  # Redirect to admin landing or another appropriate page
    else:
        form = ParentForm()

    parents = Parent.objects.all()

    return render(request, 'add_remove_parent.html', {'form': form, 'parents': parents})


@login_required
def admin_landing(request):
    return render(request, 'admin_dashboard.html')

# @login_required
#def register_management(request):
    #if request.method == 'POST':
        # Assuming you have a form to submit the pop register
       # form = PopRegisterForm(request.POST)

     #   if form.is_valid():
      #      form.save()
       #     return redirect('operator_dashboard.html')  # Redirect to operator dashboard or another appropriate page
   # else:
    #    form = PopRegisterForm()

    #pop_register_data = PopRegister.objects.all()

    #return render(request, 'register_management.html', {'form': form, 'pop_register_data': pop_register_data}) #

@login_required
def pop_register(request):
    children = Child.objects.all()  # Retrieve children from the database
    return render(request, 'pop_register.html', {'children': children})


@login_required
def add_bus_stop(request):
    if request.method == 'POST':
        form = BusStopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('operator_dashboard.html')
    else:
        form = BusStopForm()

    return render(request, 'add_bustop.html', {'form': form})


@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('operator_dashboard')
    else:
        form = ChildForm()

    return render(request, 'add_child.html', {'form': form})


@login_required
def bus_tracking(request):
    # Assuming you have a variable `bus_location` containing the bus coordinates
    bus_location = {'latitude': 37.7749, 'longitude': -122.4194}

    return render(request, 'bus_tracking.html', {'bus_location': bus_location})


@login_required
def send_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['message']
            user = request.user

            # Create a new Feedback instance and save it to the database
            Feedback.objects.create(user=user, message=message)

            # Optionally, you can provide feedback to the user that the message was sent
            return render(request, 'parentfeedbacksent.html')
    else:
        form = FeedbackForm()

    return render(request, 'send_feedback.html', {'form': form})


@csrf_protect
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard.html')
            elif user.is_staff:
                return redirect('operator_dashboard.html')
            else:
                return redirect('parent_dashboard.html')
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

@login_required
def custom_logout(request):
    logout(request)
    return redirect('login.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def operator_dashboard(request):
    return render(request, 'operator_dashboard.html')

@login_required
def parent_dashboard(request):
    return render(request, 'parent_dashboard.html')
