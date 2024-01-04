from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'user','title','desc','complete'
        ]

        labels={
            'desc':'Description',
            'complete':'is completed ?'
        }

        widgets = {
            'user': forms.HiddenInput(),  # Hide the user field in the form
        }
    
    """def __init__(self,*args,**kwargs):
        super(TaskForm,self).__init__(*args,**kwargs)
        self.fields['user'].empty_label="Select User"#10
    """

    
    
        
