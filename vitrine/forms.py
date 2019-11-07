from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label= 'Votre email')
    subject = forms.CharField(required=True, label= 'Objet du message')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Votre message')