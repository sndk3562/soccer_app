from .models import Player,EnemyPlayer,EnemyCountry,MyTeamNumber
from django import forms
from django.forms import ModelForm



def NoNeedToChagne(self):
    return True
ModelForm.has_changed = NoNeedToChagne


class GameCountryForm(forms.Form):
    my_team_number_post = forms.ModelChoiceField(queryset=MyTeamNumber.objects.all(),empty_label='あなたのチーム')
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
            'shoot': '',
        }


class PlayerForm(ModelForm):

    class Meta:
        model = Player
        fields = ('name','defence','dribble','passing','shoot' )
        num_CHOICES = ([(x, x) for x in range(0, 99)])

        labels = {
            'name': '',
            'defence': '',
            'dribble': '',
            'passing': '',
            'shoot': '',
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