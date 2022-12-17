from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    title = models.CharField(max_length=128, blank=True)
    description = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True)
    headline = models.CharField(max_length=128, blank=True)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following')
    followed_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user', )