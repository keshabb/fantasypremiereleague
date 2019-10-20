from django import forms


class BotForm(forms.Form):
    Bank_AMT = forms.IntegerField(label="Bank Amount ", label_suffix="$", initial=100, disabled=True)
    GK_AMT = forms.IntegerField(min_value=8, max_value=15, label="GK Amount ", label_suffix='$', required=False)
    DF_AMT = forms.IntegerField(min_value=25, max_value=40, label="DF Amount ", label_suffix='$', required=False)
    MD_AMT = forms.IntegerField(min_value=36, max_value=50, label="MD Amount ", label_suffix='$', required=False)
    ST_AMT = forms.IntegerField(min_value=36, max_value=50, label="ST Amount ", label_suffix='$', required=False)


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
