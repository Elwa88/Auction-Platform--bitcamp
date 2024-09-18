from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.pk} - {self.name}'

class Auction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    listing_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    min_bid = models.PositiveIntegerField(default=1)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)

    def __str__(self):
        return f'{self.product} - {self.current_bid}'
    

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=10,decimal_places=2)
    placing_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.auction} - {self.bid}'