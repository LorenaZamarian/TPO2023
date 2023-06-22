# from django import forms

# from .models import Producto, Varietal,Bodega

# class VarietalForm(forms.ModelForm):

#     class Meta:
#         model=Varietal
#         # fields='__all__'
#         fields=['nombre', 'descripcion']
#         #exclude=('baja',)
#         widgets = {
#             'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'})
#         }
#         error_messages = {
#             'nombre' :{
#                 'required':'Contesta porfa!'
#             }
#         }

# class BodegaForm(forms.ModelForm):

#     class Meta:
#         model=Bodega
#         # fields='__all__'
#         fields=['nombre', 'ubicacion', 'telefono', 'email']
#         #exclude=('baja',)
#         widgets = {
#             'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'})
#         }
#         error_messages = {
#             'nombre' :{
#                 'required':'Completa porfa!'
#             }
#         }        

# class ProductoForm(forms.ModelForm):

#     nombre=forms.CharField(
#             label='Nombre',           
#             widget=forms.TextInput(attrs={'class':'form-control'})
#         )
#     precio=forms.DecimalField(
#             label='Precio', 
#             widget=forms.DecimalField(attrs={'class':'form-control'})
#         )
#     descripcion = forms.CharField(
#         widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
#     )
#     """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
#     quiero mostrar en el selector"""
#     varietal = forms.ModelChoiceField(
#         queryset=Varietal.objects.filter(baja=False),
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#     bodega = forms.ModelChoiceField(
#         queryset=Bodega.objects.filter(baja=False),
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )

#     imagen = forms.ImageField(
#         widget=forms.FileInput(attrs={'class':'form-control'})
#     )
#     stock=forms.CharField(
#             label='Stock', 
#             widget=forms.DecimalField(attrs={'class':'form-control'})
#         )
#     cosecha=forms.CharField(
#             label='Cosecha', 
#             widget=forms.DecimalField(attrs={'class':'form-control'})
#         )


#     class Meta:
#         model=Producto
#         fields=['nombre','precio','stock','imagen','bodega','varietal','cosecha','descripcion']

