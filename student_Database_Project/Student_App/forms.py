from django import forms
from .models import Teacher
from django.core.exceptions import ValidationError

class TeacherSignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = [
            'first_name', 'middle_name', 'last_name', 'email', 'phone',
            'school_name', 'teacher_id', 'designation', 'subjects',
            'password', 'confirm_password', 'security_question'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")


from django import forms
from .models import Student
from django.core.exceptions import ValidationError

class StudentSignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirm Password'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Password'
    )

    class Meta:
        model = Student
        fields = [
            'first_name', 'middle_name', 'last_name',
            'email', 'phone', 'roll_number', 'department', 'year',
            'password', 'confirm_password', 'security_question'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-select'}),
            'security_question': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Passwords do not match.")

from django import forms

class StudentLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )

from django import forms

class TeacherLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



from django import forms
from .models import Teacher, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['password', 'security_question']
        widgets = {
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'subjects': forms.Textarea(attrs={'rows': 2}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['password', 'security_question']
        widgets = {
            'year': forms.Select(attrs={'class': 'form-control'}),
        }
