from django.views.generic import (TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.forms import modelformset_factory
from .forms import PlayerForm, GameCountryForm
from .models import Player,EnemyPlayer,MyTeamNumber
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .predict_score import predict


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "soccer/index.html"
    login_url = '/accounts/login/'

@login_required()
def MakeTeamView(request):

    NumberOfTeams = len(MyTeamNumber.objects.filter(author = request.user))

    PlayerFormSet = modelformset_factory(Player, form=PlayerForm, extra=11)
    if request.method == 'POST':
        PostFormset= PlayerFormSet(request.POST)
        print(PostFormset.has_changed())

        if PostFormset.is_valid():

            MyTeamNumber.objects.create(my_team_number=NumberOfTeams,author = request.user)

            instances = PostFormset.save(commit=False)

            for x in instances:
                print('worked')
                x.author_id = request.user.id
                x.teamnumber = NumberOfTeams
                x.save()

        return redirect(to='/make')

    else:
        formset = PlayerFormSet(None,queryset=Player.objects.none(),)

    return render(request, 'soccer/make.html', {'formset': formset, 'NumberOfTeams': range(NumberOfTeams)})



@login_required()
def Update(request,team_number):
    teamnumber = team_number
    PlayerFormset = modelformset_factory(Player,form=PlayerForm,extra=0)
    queryset = Player.objects.filter(teamnumber=teamnumber).filter(author=request.user)
    print(queryset,111)
    RequestFormset = PlayerFormset(request.POST or None,queryset=queryset)

    if RequestFormset.is_valid():
        instances = RequestFormset.save(commit=False)
        for instance in instances:
            instance.author_id = request.user.id
            instance.teamnumber = teamnumber
            instance.save()
        return redirect(to='/make')

    return render(request, 'soccer/update.html', {'formset': RequestFormset})



@login_required()
def GameView(request):

    form = GameCountryForm


    if request.method == 'POST':
        country_and_number_form = form(request.POST)
        if country_and_number_form.is_valid():
            country_number =country_and_number_form.cleaned_data
            ecn = country_number['enemy_country_name_post']
            ytn = country_number['my_team_number_post']
            Myqueryset = Player.objects.filter(teamnumber=int(str(ytn)[3])).filter(author=request.user)
            Enemyqueryset = EnemyPlayer.objects.filter(CountryName = ecn.id)###注意
            predintion = predict.main(Myqueryset,Enemyqueryset)

            return render(request, 'soccer/game.html', {'form': form,'prediction':predintion,})

    else:
        No_team_coment = []
        if not len(MyTeamNumber.objects.filter(author=request.user)):
            No_team_coment.append('チームを作成してください')

        return render(request, 'soccer/game.html', {'form': GameCountryForm,'No_team_coment':No_team_coment})