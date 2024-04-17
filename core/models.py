from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    cnpj = models.CharField(max_length=12, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    class Meta:
        db_table = "client"

    def __str__(self):
        return self.name
