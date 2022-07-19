from django import forms
from teman.models import Teman

class TemanForm(forms.ModelForm):
    class Meta:
        model = Teman
        fields = ["nama", "tanggal_lahir", "alamat", "foto"]