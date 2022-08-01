from django.db import models

# Create your models here.
class search(models.Model):
    name = models.CharField(max_length=30);
    start_date = models.DateField();
    end_date = models.DateField();

    def __str__(self):
        return self.name, self.start_date, self.end_date