from django import forms
from .models import Qurulmalar, Watch

class QurulmalarForm(forms.ModelForm):
    class Meta:
        model = Qurulmalar
        fields = '__all__'

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = '__all__'
