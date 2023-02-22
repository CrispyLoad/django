from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', min_length=3)
    age = forms.IntegerField(label='Возраст', initial="18")
    required_css_class = "field"
    error_css_class = "error"
