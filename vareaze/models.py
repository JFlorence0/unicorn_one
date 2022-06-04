from django.db import models
from account.models import Account
from datetime import datetime
from pytz import timezone

est_tz = timezone('EST')
# Create your models here.
class Contract(models.Model):
	"""An agreement between two users"""
	date_added = models.DateTimeField(default=datetime.now(est_tz))
	text = models.CharField(max_length=100)
	vareaze_id = models.CharField(max_length=12)
	sent_to = models.CharField(max_length=12)

	def __str__(self):
		# String representation
		return f"Contract initiated: {self.date_added}."

