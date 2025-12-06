from django.contrib import admin
from core.models import CatequeseAdultoModel
from core.models import CatequeseInfantilModel
from core.models import CrismaModel
from core.models import Perseveranca_MEJ_Model


class CatequeseInfantilAdmin(admin.ModelAdmin):
    list_display = ('nome','data_nascimento','criado_em')
    date_hierarchy = 'criado_em'
    search_fields = ('nome','data_nascimento','criado_em')

class CatequeseAdultoAdmin(admin.ModelAdmin):
    list_display = ('nome','data_nascimento','criado_em')
    date_hierarchy = 'criado_em'
    search_fields = ('nome','data_nascimento','criado_em')

class CrismaAdmin(admin.ModelAdmin):
    list_display = ('nome','data_nascimento','criado_em')
    date_hierarchy = 'criado_em'
    search_fields = ('nome','data_nascimento','criado_em')

class Perseveranca_MEJ_Admin(admin.ModelAdmin):
    list_display = ('nome','data_nascimento','criado_em')
    date_hierarchy = 'criado_em'
    search_fields = ('nome','data_nascimento','criado_em')

admin.site.register(CatequeseInfantilModel, CatequeseInfantilAdmin)
admin.site.register(CatequeseAdultoModel, CatequeseAdultoAdmin)
admin.site.register(CrismaModel, CrismaAdmin)
admin.site.register(Perseveranca_MEJ_Model, Perseveranca_MEJ_Admin)