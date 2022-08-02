from django.db import models

# Create your models here.
class stock(models.Model):
    date = models.DateTimeField();
    open = models.DecimalField(max_digits=10, decimal_places=2);
    high = models.DecimalField(max_digits=10, decimal_places=2);
    low = models.DecimalField(max_digits=10, decimal_places=2);
    close = models.DecimalField(max_digits=10, decimal_places=2);
    adj_close = models.DecimalField(max_digits=10, decimal_places=2);
    volume = models.BigIntegerField();

    def __str__(self):
        return str(self.date)
    