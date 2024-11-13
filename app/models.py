from django.db import models

class URL(models.Model):
    original_url = models.URLField()  # Store the original URL
    short_code = models.CharField(max_length=6, unique=True)  # Store the shortened code (6 chars is a good length)
    number_of_time = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"
