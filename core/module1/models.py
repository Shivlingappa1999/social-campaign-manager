from django.db import models

class Campaign(models.Model):
    PLATFORM_CHOICES = [
        ("Instagram", "Instagram"),
        ("Facebook", "Facebook"),
        ("Twitter", "Twitter"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Paused", "Paused"),
        ("Completed", "Completed"),
    ]

    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
