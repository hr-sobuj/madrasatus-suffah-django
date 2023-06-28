from django import forms
from .models import Teacher 

class UpdateProfileForm(forms.ModelForm):
    teacher_name=forms.CharField(required=False,label="Name",widget=forms.TextInput(attrs={'placeholder':"Your Name"}))
    teacher_designation=forms.CharField(required=False,label="Designation",widget=forms.TextInput(attrs={'placeholder':"Your Designation"}))
    teacher_comment=forms.CharField(required=False,label="Comment",widget=forms.Textarea(attrs={'placeholder':"Your Comment"}))
    teacher_details=forms.CharField(required=False,label="Details",widget=forms.Textarea(attrs={'placeholder':"Your Info"}))
    teacher_image=forms.ImageField(required=False,label="Image")
    class Meta:
        model = Teacher
        fields = ['teacher_name','teacher_designation','teacher_details','teacher_comment','teacher_image']