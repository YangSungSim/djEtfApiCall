from django.db import models

# Create your models here.
class search(models.Model):
    name = models.CharField(max_length=30);
    start_date = models.CharField(max_length=8);
    end_date = models.CharField(max_length=8);

    def __str__(self):
        return self.name+" "+str(self.start_date)+" "+str(self.end_date)