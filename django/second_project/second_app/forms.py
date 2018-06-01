from django import forms 
from second_app.models import User

# class PersonalData(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email =forms.EmailField()

class PersonalData(forms.ModelForm):
    # FORM FIELDS CAN BE TAKE DIRECTLY FROM MODEL
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email =forms.EmailField()

    class Meta:
        model = User
        fields = '__all__'
