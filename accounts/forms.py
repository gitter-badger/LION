from django import forms
from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = (
            "last_name", "first_name", 
            "last_name_kana", "first_name_kana",
            "username", "faculty", "grade", "email", "telephone", "rawpassword"
        )
