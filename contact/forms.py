from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label= "Nombre", widget=forms.TextInput(attrs={'placeholder': 'Introduce tu Nombre',
                                                                                                         "class":"form-control"}))   
    email = forms.EmailField(required=True, label="Correo electrónico",  widget=forms.TextInput(attrs={'placeholder': 'Introduce tu correo electrónico',
                                                                                                         "class":"form-control"}))
    content = forms.CharField(required=True, label="Mensaje",  widget=forms.Textarea(attrs={'placeholder': 'Escribe aquí tu mensaje',
                                                                                                         "class":"form-control",
                                                                                                         "rows": 3}))
    
