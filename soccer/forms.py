from .models import Player,EnemyPlayer,EnemyCountry,MyTeamNumber
from django import forms
from django.forms import ModelForm


def changeOk(self):
    return True
ModelForm.has_changed = changeOk


class GameCountryForm(forms.Form):
    my_team_number_post = forms.ModelChoiceField(queryset=MyTeamNumber.objects.all(),empty_label='あなたのチーム')
    # Your_team_number = forms.IntegerField(label='あなたのチーム',widget=forms.TextInput(
    #         attrs={'placeholder':'あなたのチーム'}))
    enemy_country_name_post = forms.ModelChoiceField(queryset=EnemyCountry.objects.all(),label='相手のチーム',empty_label='相手のチーム')

class EnemyCountryForm(forms.Form):
    country_name = forms.ModelChoiceField(queryset=EnemyCountry.objects.all())

class EnemyPlayerForm(ModelForm):
    class Meta:
        model = EnemyPlayer
        fields = ('name','defence','dribble','passing','shoot','CountryName' ) #author#teamnumber
        num_CHOICES = ([(x, x) for x in range(0, 99)])
        labels = {
            'name': '',
            'defence': '',
            'dribble': '',
            'passing': '',
            'shoot':'',
        }





class PlayerForm(ModelForm):

    class Meta:
        model = Player
        fields = ('name','defence','dribble','passing','shoot' ) #author#teamnumber
        num_CHOICES = ([(x, x) for x in range(0, 99)])

        labels = {
            'name': '',
            'defence': '',
            'dribble': '',
            'passing': '',
            'shoot':'',
        }

        widgets = {
            'defence': forms.Select(choices=num_CHOICES, attrs={'class': 'form-control'}),
            'dribble': forms.Select(choices=num_CHOICES, attrs={'class': 'form-control'}),
            'passing': forms.Select(choices=num_CHOICES, attrs={'class': 'form-control'}),
            'shoot': forms.Select(choices=num_CHOICES, attrs={'class': 'form-control'}),
            #'author':forms.HiddenInput,
            #'teamnumber': forms.HiddenInput
        }

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['name'].initial = 'a'
        self.fields['defence'].initial = 50
        self.fields['dribble'].initial = 50
        self.fields['passing'].initial = 50
        self.fields['shoot'].initial = 50











    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['author'].widget = forms.HiddenInput()
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['teamnumber'].widget = forms.HiddenInput()

'''
class PlayerForm(forms.Form):
    name = forms.CharField(max_length=5,initial='a')
    defence = forms.IntegerField(initial=1)
    dribble = forms.IntegerField(initial=1)
    passing = forms.IntegerField(initial=1)
    shoot =  forms.IntegerField(initial=1)
'''
'''
class PlayerForm(forms.Form):
    name = forms.CharField(max_length=20,initial='a')
    defence = forms.TypedChoiceField(choices=[(x, x) for x in range(0, 99)], coerce=int,initial=50)
    dribble = forms.TypedChoiceField(choices=[(x, x) for x in range(0, 99)], coerce=int,initial=50)
    passing = forms.TypedChoiceField(choices=[(x, x) for x in range(0, 99)], coerce=int,initial=50)
    shoot =  forms.TypedChoiceField(choices=[(x, x) for x in range(0, 99)], coerce=int,initial=50)
'''
'''
    class Meta:
        model = Player
        fields = ('name','defence','dribble', 'passing', 'shoot')
'''




