from django import forms


from .models import *
from .serializers import ImageSerializer


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)


