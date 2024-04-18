from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    cnpj = models.CharField(max_length=30, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    class Meta:
        db_table = "client"

    def __str__(self):
        return self.name


class ClientEmployee(models.Model):
    id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=30, blank=False, null=False, unique=True)
    role = models.CharField(max_length=30, blank=False, null=False)
    salary = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    class Meta:
        db_table = "client_employee"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
