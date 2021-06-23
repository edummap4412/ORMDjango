from django.contrib import admin
from .models import Chassi, Carro, Montadora


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'chassi', 'preco', 'montadora', 'get_motoristas')
    """
    essa funçoes  foi usada pois quando coloquei motoristas no list_diplay , foi me dado um erro.
    entao alterei para get_motoristas e criei um list compreresion para isso . em seguida passei 
    " get_motoristas.short_description = 'Motoristas'" para mudar o nome do header para motoristas 
    """
    def get_motoristas(self,obj):
        return ', '.join([m.username for m in obj.motoristas.all()])

    get_motoristas.short_description = 'Motoristas'


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome', )

