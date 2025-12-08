from django import forms
from web.models import Slider, Legacy, Aboutbox, ProductCategory, ProductFeature, Product, GalleryCategory, Galleryimage



class ManagerLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username (Email)"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )


# Slider form
class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title', 'image']

# Legacy form
class LegacyForm(forms.ModelForm):
    class Meta:
        model = Legacy
        fields = ['title', 'image']

# Aboutbox form
class AboutboxForm(forms.ModelForm):
    class Meta:
        model = Aboutbox
        fields = ['title', 'image']

# ProductCategory form
class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'title', 'image', 'description']

# ProductFeature form
class ProductFeatureForm(forms.ModelForm):
    class Meta:
        model = ProductFeature
        fields = ['name']

# Product form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'brandlogo', 'description', 'category', 'features']
        widgets = {
            'features': forms.CheckboxSelectMultiple()  # ManyToManyField can be handled with checkboxes
        }

# GalleryCategory form
class GalleryCategoryForm(forms.ModelForm):
    class Meta:
        model = GalleryCategory
        fields = ['name', 'image']

# Galleryimage form
class GalleryimageForm(forms.ModelForm):
    class Meta:
        model = Galleryimage
        fields = ['name', 'image', 'category']
