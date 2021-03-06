from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
import django.forms as forms
from django.core.files.images import get_image_dimensions
from .models import ShopUser

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = {'username', 'password'}

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username',
                  'password1',
                  'password2',
                  'email',
                  'age',
                  'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды!')

        return data

    def clean_avatar(self):
        data = self.cleaned_data['avatar']
        if data and len(data) > (10 * 1024):
            raise forms.ValidationError('Размер аватара не должен превышать 10МБ!')

        return data

class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
            if field_name == 'username' or field_name == 'email':
                field.widget.attrs['readonly'] = True

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data

    def clean_avatar(self):
        data = self.cleaned_data['avatar']
        if data and len(data) > (10000 * 1024):
            raise forms.ValidationError('Размер аватара не должен превышать 10МБ!')
        if data:
            w, h = get_image_dimensions(data)
            max_w = max_h = 1500
            if w > max_w or h > max_h:
                raise forms.ValidationError('Размер аватара не должен превышать %s x %d px.' % (max_h, max_w))

        return data

