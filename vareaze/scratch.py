from django.db import models
from datetime import datetime
from pytz import timezone

format = "%Y-%m-%d"
now_est = datetime.now(timezone('EST'))
print(now_est.strftime(format))
