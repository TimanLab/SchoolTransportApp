# forms.py

from django import forms
from .models import Child, BusStop
from .models import Parent
from .models import BusMileage
from .models import PopRegister, Exclusion

class PopRegisterForm(forms.ModelForm):
    class Meta:
        model = PopRegister
        fields = ['child', 'operator', 'status']

class ExclusionForm(forms.ModelForm):
    class Meta:
        model = Exclusion
        fields = ['child', 'reason']


class BusMileageForm(forms.ModelForm):
    class Meta:
        model = BusMileage
        fields = ['bus', 'initial_mileage']


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name']

class ChildForm(forms.Form):
    name = forms.CharField(max_length=100)
    ucs_number = forms.CharField(max_length=20)
    grade = forms.CharField(max_length=10)

class BusStopForm(forms.Form):
    bus_stage_name = forms.CharField(max_length=100)
    pick_drop_time = forms.TimeField()


class FeedbackForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
