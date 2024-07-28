from django.db import models


class Identity(models.Model):
    """model for Identity for global Db."""

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    is_spam = models.IntegerField(default=0)

    class Meta:
        unique_together = ('first_name', 'last_name', 'phone', 'email', 'is_spam')

    def __str__(self):
        return f"{self.phone}"


class Registered(models.Model):
    """model for Registered Users."""

    phone = models.CharField(max_length=64, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"{self.phone}"


class RegisteredToSaved(models.Model):
    """model for relating registered user with their saved contacts."""

    registered_user = models.ForeignKey(Registered, on_delete=models.CASCADE)
    contact_saved = models.ForeignKey(Identity, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.registered_user} saved {self.contact_saved}"
