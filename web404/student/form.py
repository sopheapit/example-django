from django import forms

class Contactform(forms.Form):
    full_name=forms.CharField(max_length=200,
                              widget=forms.TextInput(
                                  attrs={'class':'col-xs-12 col-sm-6 form-control'}))
    phone=forms.CharField(max_length=100,
                          widget=forms.TextInput(
                              attrs={'class':'col-xs-12 col-sm-6 form-control'}))
    email = forms.CharField(max_length=100,
                            widget=forms.TextInput(
                                attrs={'class':'col-xs-12 col-sm-6 form-control'}))
    detail=forms.CharField(widget=forms.Textarea(
        attrs={'class':'col-xs-12 col-sm-12 form-control'}))
class Staffform(forms.Form):
    full_name = forms.CharField(max_length=200,
    widget = forms.TextInput(
        attrs={'class': 'col-xs-12 col-sm-6 form-control'})
    )
    gender = forms.CharField(max_length=50,
                             widget=forms.TextInput(
                                 attrs={'class': 'col-xs-12 col-sm-6 form-control'})
                             )
    phone = forms.CharField(max_length=50,
                            widget=forms.TextInput(
                                attrs={'class': 'col-xs-12 col-sm-6 form-control'})
                            )
    email = forms.CharField(max_length=100,widget = forms.TextInput(
        attrs={'class': 'col-xs-12 col-sm-6 form-control'}))
    address = forms.CharField(widget=forms.Textarea(
        attrs={'class':'col-xs-12 col-sm-12 form-control'}))
    photo = forms.ImageField(required=False)