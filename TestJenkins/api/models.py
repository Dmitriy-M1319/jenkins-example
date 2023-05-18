from django.db import models

class CarModel(models.Model):
    mark = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    engine = models.CharField(max_length=40)
    cylyner_count = models.IntegerField()
    oil_type = models.IntegerField()

    class Meta:
        db_table = 'cars'
