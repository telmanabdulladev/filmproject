from django import forms # we launced to import forms from django library
from app_film.models import FilmModel # we launched to import FilmModel here from app_film.models due to usage

# class FilmForm(forms.ModelForm):
#     class Meta:
#         model=FilmModel
#         fields=('name','poster','video','rating','about')
class FilmForm(forms.Form):
    name=forms.CharField(label="Name", max_length=256,widget=forms.TextInput(attrs={'class': 'form-control'}))
    poster=forms.ImageField(label="Poster", widget=forms.FileInput(attrs={'class': 'form-control','id':'exampleFormControlInput2'}))
    video=forms.FileField(label="Video", widget=forms.FileInput(attrs={'class': 'form-control','id':'exampleFormControlInput3'}))
    rating=forms.FloatField(label="Rating", widget=forms.NumberInput(attrs={'class': 'form-control','id':'exampleFormControlInput4'}))
    pub_date=forms.DateField(label="Published date", widget=forms.DateInput(attrs={'class': 'form-control','id':'exampleFormControlInput5'}))
    views_count=forms.IntegerField(label="Views Count", widget=forms.NumberInput(attrs={'class': 'form-control','id':'exampleFormControlInput6'}))
    about=forms.CharField(label="About", widget=forms.Textarea(attrs={'class': 'form-control','id':'exampleFormControlInput7'}))



    
