from django import forms
from mptt.forms import TreeNodeChoiceField
from heirarchical_data_mptt.models import Filer

class NewFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    parent = TreeNodeChoiceField(queryset=Filer.objects.all())