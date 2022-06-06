from django.db import models
from account.models import Account
from datetime import datetime
from pytz import timezone

est_tz = timezone('EST')
tz_format = "%Y-%m-%d"
# Create your models here.
class Contract(models.Model):
	"""An agreement between two users"""
	owner = models.ForeignKey(Account, on_delete = models.PROTECT)
	date_added = models.DateTimeField(default=datetime.now(est_tz).strftime("%Y-%m-%d"))
	vareaze_id = models.CharField(max_length=12)
	sent_to = models.CharField(max_length=12)

	def __str__(self):
		# String representation
		return f"Contract initiated: {str(self.date_added)[:10]} with {self.sent_to}"

