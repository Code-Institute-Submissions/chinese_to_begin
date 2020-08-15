from django import forms
from .models import Store, Category


class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Store
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.item():
            field.widget.attrs['class'] = 'border-dark rounded-1'