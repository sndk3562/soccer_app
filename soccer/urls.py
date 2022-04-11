from mysite.urls import  path
from .views import make_test_formset,Update,GameView

urlpatterns = [
    path('', make_test_formset,name='make_team'),

    path('update/<int:team_number>',Update,name='update'),
    path('game/',GameView,name='game')
]