from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        ordering = ["first_name"]
