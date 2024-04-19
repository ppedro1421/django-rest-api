from django.db import models


class Employer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    class Meta:
        db_table = "employer"

    def __str__(self):
        return self.name


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, blank=False, null=False)
    description = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        db_table = "employee_role"

    def __str__(self):
        return self.description


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, blank=False, null=False)
    salary = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
