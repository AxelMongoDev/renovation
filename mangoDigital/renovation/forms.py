from django import forms
from .models import BussinessContact
from django.template.defaultfilters import mark_safe

class BussinessContactForm(forms.ModelForm):
    businessName = forms.CharField(label=mark_safe
    ('<span style="font-weight: bold; font-size:72%;">Nombre</span>'),
    widget=forms.TextInput(attrs={"placeholder":"Introduce aquí tu nombre",
    "class":"form-control form-text text-muted form-group",
    "style":"font-size: small;", "id":"my-businessName"}))

    businessPhone = forms.CharField(label = mark_safe
    ('<span style="font-weight: bold; font-size:72%;">Teléfono</span>'),
    widget=forms.TextInput(attrs={"placeholder":"Introduce aquí tu número de teléfono",
    "class":"form-control form-text text-muted form-group",
    "style":"font-size: small;","id":"my-businessPhone"}))

    businessEmail = forms.CharField(label = mark_safe
    ('<span style="font-weight: bold; font-size:72%;">Correo electrónico</span>'),
    widget=forms.TextInput(attrs={"placeholder":"Introduce aquí tu correo electrónico",
    "class":"form-control form-text text-muted form-group",
    "style":"font-size: small;","id":"my-businessEmail"})) 

    businessComment = forms.CharField(label = mark_safe
    ('<span style="font-weight: bold; font-size:72%;">¡Dejanos un comentario!</span>'),
    widget=forms.Textarea(attrs={"rows":2, "cols":5, "placeholder":"Platícanos de que empresa nos contactas y en que servicios estas interesado.",
    "class":"form-control form-text text-muted form-group",
    "style":"font-size: small;","id":"my-businessComment"}))

    def clean(self):
        super(BussinessContactForm,self).clean()
        businessName = self.cleaned_data.get("businessName")
        businessPhone = self.cleaned_data.get("businessPhone")
        businessEmail = self.cleaned_data.get("businessEmail")
        businessComment = self.cleaned_data.get("businessComment")

    class Meta:
        model = BussinessContact
        fields = ["businessName","businessPhone","businessEmail","businessComment"]