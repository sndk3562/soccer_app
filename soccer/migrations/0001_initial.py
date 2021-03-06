# Generated by Django 4.0.3 on 2022-04-14 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EnemyCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enemy_country_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='選手名')),
                ('defence', models.IntegerField(verbose_name='ディフェンス')),
                ('dribble', models.IntegerField(verbose_name='ドリブル')),
                ('passing', models.IntegerField(verbose_name='パス')),
                ('shoot', models.IntegerField(verbose_name='シュート')),
                ('teamnumber', models.IntegerField(max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyTeamNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_team_number', models.IntegerField(max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EnemyPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='選手名')),
                ('defence', models.IntegerField(verbose_name='ディフェンス')),
                ('dribble', models.IntegerField(verbose_name='ドリブル')),
                ('passing', models.IntegerField(verbose_name='パス')),
                ('shoot', models.IntegerField(verbose_name='シュート')),
                ('CountryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccer.enemycountry')),
            ],
        ),
    ]
