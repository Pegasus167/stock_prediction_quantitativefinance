from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=256, blank=True)
    symbol = models.CharField(max_length=256, blank=True)
    industry = models.CharField(max_length=256, blank=True)
    isinCode = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_company_by_id(pk):
        return Company.objects.get(pk=pk)