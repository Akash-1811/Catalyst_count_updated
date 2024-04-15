from django.db import models

# Create your models here.

class Companies(models.Model):
    company_id = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_domain = models.CharField(max_length=255)
    year_founded = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    linked_in_url = models.CharField(max_length=255)
    current_employee_est = models.CharField(max_length=255)
    total_employee_est = models.CharField(max_length=255)

    def __str__(self):
        return str(self.company_name)

    class Meta:
        # Define indexes for country and locality fields
        indexes = [
            models.Index(fields=['country']),
            models.Index(fields=['locality']),
        ]
