import uuid
from django.db import models


class Employer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=False, null=False, auto_now=True)

    class Meta:
        db_table = "employer"

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employer = models.ForeignKey(Employer, related_name="employees", on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    role = models.CharField(max_length=30, blank=False, null=False)
    salary = models.IntegerField(blank=False, null=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=False, null=False, auto_now=True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
