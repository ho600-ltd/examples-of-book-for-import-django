from django.db import models


class EndSpot(models.Model):
    topic = models.CharField(max_length=150, unique=True)
    note = models.TextField()

    class Meta:
        permissions = (
            ('add_flowdata_under_this_end_spot', 'Add FlowData records under This EndSpot'),
        )

class FlowData(models.Model):
    end_spot = models.ForeignKey(EndSpot, on_delete=models.CASCADE)
    timestamp = models.DecimalField(max_digits=20, decimal_places=6, db_index=True)
    value = models.FloatField() #IFNO: in some cases, DecimalField is better
    create_time = models.DateTimeField(auto_now_add=True, db_index=True)