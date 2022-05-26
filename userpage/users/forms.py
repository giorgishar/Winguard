from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser
from django import forms
import math, random



"""
1. Random OTP
2. login view 
    - if active -> cannot login with otp
    - if not active -> can login with only otp -> redirect to change password
3. password change view
    - 2 fields - password password2
    - password == password2 
    - validators -> password_validator
    - user.set_password(password)
    - user.is_acitve = True
    - user.save()
"""

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username']

    def save(self, commit=True):
        user = super().save(commit=False)
        # user.set_password(
        #     'admin12'
        # )
        string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        OTP = ""
        length = len(string)
        for i in range(8) :
            OTP += string[math.floor(random.random() * length)]
        user.otp = OTP
        if commit:
            user.save()
        return user



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


# class PasswordChange(forms.Form):
#     new_password = forms.PasswordInput()
#     reenter_password = forms.PasswordInput()

#     def clean(self):
#         new_password = self.cleaned_data.get('new_password')
#         reenter_password = self.cleaned_data.get('reenter_password')
#         if new_password == reenter_password:
            
#             return self.cleaned_data
#         else:
#             return "Passwords doesn't match"


class PasswordChange(forms.ModelForm):
    model = CustomUser
    fields = ['new_password1', 'new_password2']