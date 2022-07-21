import django


from django.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text', )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'id': 'floatingTextarea2', 'class': 'form-control', 'placeholder': 'What\'s on mind ?', 'style': 'height: 180px'})
