from django.db import models
from django.contrib.auth import get_user_model


class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('nome',max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0] # padrao devolve (objeto, boolean)

class Carro(models.Model):
    """"
    #OneToOne
    Cada carro só pode se relacionar com um chassi e cada chassi só pode se
    relacionar com um carro.

    #ForeignKey ( One to Many )
    Cada carro tem uma montadoras mas uma montadora pode montar varios carros.

    # ManyToMany
    Um carro pode ser dirigido por vários motoristas
    e um motorista pode dirigir diversos carros.

    ATENÇÃO
    se precisar setar um valor defalut faça:
    montadora = models.ForeignKey(Montadora, SET_DEFAULT, default=1)

    a Função get_or_create ir criat uma montadora caso ela na exista
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    #montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('models', max_length=30, help_text='Máximo 30 caracteres')
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.modelo} {self.montadora}'


