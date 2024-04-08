from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import BooleanField
from django import forms

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
        )
        model.is_active = False


class UserProfileForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "country",
            "phone",
            "avatar",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()
