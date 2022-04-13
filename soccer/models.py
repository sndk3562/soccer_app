from django.db import models
from django.conf import settings


class MyTeamNumber(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    my_team_number = models.IntegerField(max_length=10)
    def __str__(self):
        return ('チーム'+str(self.my_team_number))

class Player(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField('選手名',max_length=20)
    defence = models.IntegerField('ディフェンス')
    dribble = models.IntegerField('ドリブル')
    passing =  models.IntegerField('パス')
    shoot = models.IntegerField('シュート')
    teamnumber = models.IntegerField(max_length=10)
    def __str__(self):
        return self.name


class EnemyCountry(models.Model):

    enemy_country_name = models.CharField(max_length=20)

    def __str__(self):
        return self.enemy_country_name

class EnemyPlayer(models.Model):

    name = models.CharField('選手名', max_length=20)
    defence = models.IntegerField('ディフェンス',)
    dribble = models.IntegerField('ドリブル')
    passing = models.IntegerField('パス')
    shoot = models.IntegerField('シュート')
    CountryName = models.ForeignKey(EnemyCountry,on_delete=models.CASCADE)
    def __str__(self):
        return self.name