from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from . models import User, Professor, Grade
from django.forms import ModelForm


class ProfessorRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    # contact = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.is_professor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        professor = Professor.objects.create(user=user)
        # professor.contact = self.cleaned_data.get('contact')
        professor.save()
        return user


# class gradesForm(ModelForm):
#     class Meta:
#         model = Grade 
#         fields = '__all__'
