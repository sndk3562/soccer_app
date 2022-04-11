from django.shortcuts import render
from django.views.generic import TemplateView
from django.forms import modelformset_factory
from django.forms import formset_factory
from .forms import PlayerForm,EnemyCountryForm,GameCountryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Player,EnemyPlayer,MyTeamNumber
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .predict_score import predict
import main

import inspect

# def changeOk(self):
#     return False
# modelformset_factory.has_changed = changeOk

@login_required()
def make_test_formset(request):

    NumberOfTeams = len(MyTeamNumber.objects.filter(author = request.user))

    PlayerFormSet = modelformset_factory(Player, form=PlayerForm, extra=11)
    if request.method == 'POST':
        PostFormset= PlayerFormSet(request.POST)
        print(PostFormset.has_changed())

        if PostFormset.is_valid():
            print('ok')
            MyTeamNumber.objects.create(my_team_number=NumberOfTeams,author = request.user)

            instances = PostFormset.save(commit=False)

            for x in instances:
                print('worked')
                x.author_id = request.user.id
                x.teamnumber = NumberOfTeams
                x.save()
                # x.cleaned_data['id'] = request.user.id
                # x.cleaned_data['teamnumber'] = 3
                # print('x', x.cleaned_data)
                # x.save()

        return redirect(to='/soccer/')

    else:
        formset = PlayerFormSet(None,queryset=Player.objects.none(),)

    return render(request, 'soccer/index.html', {'formset': formset, 'NumberOfTeams': range(NumberOfTeams)})



@login_required()
def Update(request,team_number):
    teamnumber = team_number
    PlayerFormset = modelformset_factory(Player,form=PlayerForm,extra=0)
    queryset = Player.objects.filter(teamnumber=teamnumber).filter(author=request.user)
    RequestFormset = PlayerFormset(request.POST or None,queryset=queryset)

    if RequestFormset.is_valid():
        print('ok')
        instances = RequestFormset.save(commit=False)
        for instance in instances:
            instance.author_id = request.user.id
            instance.teamnumber = teamnumber
            instance.save()
        return redirect(to='/soccer/')

    return render(request, 'soccer/update.html', {'formset': RequestFormset})



class Try (TemplateView):
    template_name = 'soccer/try.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teamnumber = self.kwargs['team_number']
        queryset = Player.objects.filter(author=self.request.user,teamnumber = teamnumber )
        formsets = formset_factory(
            form=PlayerForm,
            extra=11,
        )
        formsets2 = formsets(initial=[team.values for team in queryset])

        return {'formsets':formsets2}






@login_required()
def GameView(request):

    form = GameCountryForm
    x =[]


    if request.method == 'POST':
        country_and_number_form = form(request.POST)
        if country_and_number_form.is_valid():
            country_number =country_and_number_form.cleaned_data
            ecn = country_number['enemy_country_name_post']
            ytn = country_number['my_team_number_post']
            Myqueryset = Player.objects.filter(teamnumber=int(str(ytn)[3])).filter(author=request.user)
            Enemyqueryset = EnemyPlayer.objects.filter(CountryName = ecn.id)###注意
            predintion = main.main(Myqueryset,Enemyqueryset)

            return render(request, 'soccer/game.html', {'form': form,'prediction':predintion,})

    else:
        No_team_coment = []
        if not len(MyTeamNumber.objects.filter(author=request.user)):
            No_team_coment.append('チームを作成してください')

        return render(request, 'soccer/game.html', {'form': GameCountryForm,'x':x,'No_team_coment':No_team_coment})


