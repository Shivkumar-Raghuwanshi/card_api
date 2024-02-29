from django.db import models

# Create your models here.
class Card(models.Model):
    card_id = models.CharField(max_length=100)
    user_contact = models.CharField(max_length=100)

class Delivered(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    comment = models.CharField(max_length=100)

class DeliveryException(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    comment = models.CharField(max_length=100)

class Pickup(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

class Returned(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
