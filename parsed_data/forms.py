from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class searchNickForm(forms.Form):
    search_nick = forms.CharField(help_text="Enter the nickname.")

    def clean_search_nick(self):
        data = self.cleaned_data['search_nick']

        # Remember to always return the cleaned data.
        return data