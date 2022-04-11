from django.contrib import admin
from soccer.models import EnemyPlayer,EnemyCountry
from django.forms import modelformset_factory,formset_factory
from soccer.forms import EnemyPlayerForm


class Fileline(admin.TabularInline):
    model = EnemyPlayer
    extra = 11
class PostAdmin(admin.ModelAdmin):
    inlines = [Fileline]


admin.site.register(EnemyCountry,PostAdmin)
