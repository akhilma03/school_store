from django import forms
from .models import NewEntery,Course,Department

class NewEntryForm(forms.ModelForm):
    class Meta:
        model = NewEntery
        fields= '__all__'
    
    def __init__(self, *args, **kwargs):
        super(NewEntryForm,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['dob'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['age'].widget.attrs.update({'class':'form-control'})
        self.fields['gender'].widget.attrs.update({'class':'form-control'})
        self.fields['phone'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['address'].widget.attrs.update({'class':'form-control'})
        self.fields['department'].widget.attrs.update({'class':'form-control'})
        self.fields['course'].widget.attrs.update({'class':'form-control'})
        
        self.fields['purpose'].widget.attrs.update({'class':'form-control'})
        self.fields['materials']
        
        self.fields['course'].queryset=Course.objects.none()
        
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset =Course.objects.filter(department_id=department_id).order_by('Name')
            except (ValueError, TypeError):
                 pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:     
            self.fields['course'].queryset = self.instance.department.course_set.order_by('Name')