from django import forms  
from common.models import UserProfile, SocialAccauntProfile  
  
  
class ProfileCreationForm(forms.ModelForm):  
  
    class Meta:  
        model = UserProfile  
        fields = ['name', 'age', 'city']
        labels = {'name':'Имя', 'age':'Возраст', 'city':'Город' }


class ProfileSocAccCreationForm(forms.ModelForm):  
  
    class Meta:  
        model = SocialAccauntProfile
        # fields = '__all__'  
        fields = ['name', 'age', 'city']
        labels = {'name':'Имя', 'age':'Возраст', 'city':'Город' }