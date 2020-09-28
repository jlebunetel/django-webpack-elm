from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label=_("first name").capitalize())
    last_name = forms.CharField(max_length=150, label=_("last name").capitalize())

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user
