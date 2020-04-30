from django.db import models
from django.contrib.auth.models import User

import datetime

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    curator = models.ForeignKey('Curator', on_delete=models.DO_NOTHING)

    def __str__(self):
        try:
            return str(self.user)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Curator(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Подразделение/куратор'
        verbose_name_plural = 'Подразделение/кураторы'


class FinanceCosts(models.Model): #  A 1000      B 2000
    total = models.FloatField(verbose_name="сумма 4-x кварталов")
    title = models.CharField(
        verbose_name="название статьи",
        max_length=100,
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Статья финансирования'
        verbose_name_plural = 'Статьи финансирования'


class CuratorFinanceYear(models.Model):
    total = models.FloatField(
        verbose_name='Итоговая сумма на год со всех статей'
    )
    curator = models.ForeignKey(Curator,
                                verbose_name='Куратор',
                                on_delete=models.DO_NOTHING
    )
    year = models.IntegerField(default=datetime.date.today().year)

    def __str__(self):
        try:
            return str(self.curator) + str(self.year)
        except:
            return 'Ошибка в данных'



class CuratorFinanceQuart(models.Model):
    class QuartChoices:
        ch = [(1,'I'),(2,'II'),(2,'III'),(4,'IV')]

    finance_year = models.ForeignKey(CuratorFinanceYear,
                                     verbose_name='Финансовй год куратора',
                                     on_delete=models.DO_NOTHING
    )
    finance_cost = models.ForeignKey(FinanceCosts,
                                     verbose_name='Статья финансирования',
                                     on_delete=models.DO_NOTHING
    )
    quart = models.IntegerField(choices=QuartChoices.ch)
    total = models.FloatField(default=0)

    def __str__(self):
        try:
            return str(self.quart) + str(self.finance_cost) + str(self.finance_year)
        except:
            return 'Ошибка в данных'


class Contract(models.Model):
    curator = models.ForeignKey(Curator, on_delete=models.DO_NOTHING)
    finance_cost = models.ForeignKey(FinanceCosts, on_delete=models.DO_NOTHING)



