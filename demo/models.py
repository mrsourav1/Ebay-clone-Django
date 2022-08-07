from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date, datetime
from django.utils import timezone

class User(AbstractUser):
    pass

class Bid(models.Model):
	bid_price = models.DecimalField(max_digits=6, decimal_places=2)
	date = models.DateTimeField(default=timezone.now)
	bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
	def __str__(self): 
		return f"{self.id} - Bid Price: {str(self.bid_price)}, Date: {str(self.date)}"

class CATEGORY_CHOICES:
	CATEGORY_CHOICES = [
		# (None, ''),
		('FASHION','Fashion'),
		('TOYS', 'Toys'),
		('ELECTRONICS','Electronics'),
		('HOME','Home'),
		('SPORTS','Sports'),
	]

class Listing(models.Model):
	title = models.CharField(max_length=64)
	description = models.TextField(blank=True, default=None)
	date = models.DateTimeField(default=timezone.now)
	starting_bid = models.DecimalField(max_digits=5, decimal_places=2)
	current_bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name= "bid_listing", default=None, blank=True, null=True)
	picture = models.URLField(default="", blank=True)
	sold = models.BooleanField(default=False)
	category = models.CharField(
		max_length=11
		,choices=CATEGORY_CHOICES.CATEGORY_CHOICES
		,default=None
		,blank=True
		,null=True # TODO might want to delete this
	)
	poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings")
	watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
	def __str__(self):
		return f"{self.id} - Title: {self.title}, Starting Bid: {str(self.starting_bid)}"

class Comment(models.Model):
	comment_text = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comments")
	poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
	def __str__(self): 
		return f"{self.id} - Text: {self.comment_text}, Date: {str(self.date)}"




























