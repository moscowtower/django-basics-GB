from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.files.images import get_image_dimensions

from mainapp.models import Product
from authapp.models import ShopUser

class ProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'short_description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
        self.fields['description'].widget.attrs['rows'] = 4


class AdminShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


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