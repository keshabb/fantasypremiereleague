from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BotForm(forms.Form):
    Bank_AMT = forms.IntegerField(label="Bank Amount ", label_suffix="$", initial=100, disabled=True)
    GK_AMT = forms.IntegerField(min_value=8, max_value=15, label="GK Amount (Optional)", label_suffix='$', required=False)
    DF_AMT = forms.IntegerField(min_value=25, max_value=40, label="DF Amount (Optional)", label_suffix='$', required=False)
    MD_AMT = forms.IntegerField(min_value=36, max_value=50, label="MD Amount (Optional)", label_suffix='$', required=False)
    ST_AMT = forms.IntegerField(min_value=36, max_value=50, label="ST Amount (Optional)", label_suffix='$', required=False)


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    profile = forms.ImageField(required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required')
    phone = forms.IntegerField(required=False, help_text='Optional')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'profile', 'password1', 'password2']
