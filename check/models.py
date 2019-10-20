from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User, related_name='employee', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    ip = models.CharField(max_length=30, null=True, blank=True)
    is_admin_user = models.BooleanField(default=False)
    updated_by = models.ForeignKey(User, related_name='created_employees', null=True, on_delete=models.SET_NULL)
    is_password_change = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name