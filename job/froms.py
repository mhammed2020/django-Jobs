from  django import  forms
from  .models import Apply

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','cv','coverLetter']
