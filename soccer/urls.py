from django.urls import path
from soccer import views
from mysite.urls import  path
from .views import MakeTeamView,Update,GameView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('make', MakeTeamView,name='make_team'),
    path('update/<int:team_number>', Update, name='update'),
    path('game/', GameView, name='game')
]



