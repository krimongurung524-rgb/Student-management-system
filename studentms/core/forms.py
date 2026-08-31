from django import forms
from .models import Student


# ModelForm — CRUD ko lagi
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name', 'email', 'phone',
            'gender', 'grade', 'address', 'slug'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Full Name',
                'class': 'form-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-input'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-input'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-input'
            }),
            'grade': forms.Select(attrs={
                'class': 'form-input'
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Address',
                'class': 'form-input',
                'rows': 3
            }),
            'slug': forms.TextInput(attrs={
                'placeholder': 'Slug (e.g. ram-sharma)',
                'class': 'form-input'
            }),
        }


# Custom Form — for Search (forms.Form)
class StudentSearchForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by name...',
            'class': 'form-input'
        })
    )

    grade = forms.ChoiceField(
        required=False,
        choices=[('', 'All Grades')] + Student.GRADE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-input'
        })
    )

    gender = forms.ChoiceField(
        required=False,
        choices=[('', 'All Genders')] + Student.GENDER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-input'
        })
    )

    # Custom validation
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and name.isdigit():
            raise forms.ValidationError(
                "Name number matra huna sakdaina!"
            )
        return name