from django.db import models
from django.utils import timezone

# Create your models here.

class Machine(models.Model):
    HALL_NUMBER = (
        ('1', '1501'),
        ('2', '1502'),
        ('3', '1503'),
        ('4', '1504'),
        ('5', '1505'),
        ('6', '1506'),
        ('7', '1507'),
    )
    TYPES_MAC = (
        ('W', 'Washer'),
        ('D', 'Dryer'),
    )
    HALL_SIDE = (
        ('AD', 'A/D Side'),
        ('BC', 'B/C Side'),
    )
    AVAILABLE = 'Available'
    IN_USE = 'In Use'
    CYCLE_COMPLETE = 'Cycle Complete'
    UNAVAILABLE = 'Unavailable'
    AVAILABILITIES = (
            (AVAILABLE, 'Available'),
            (IN_USE, 'In Use'),
            (CYCLE_COMPLETE, 'Cycle Complete'),
            (UNAVAILABLE, 'Unavailable'),
    )
    
    hall = models.CharField(max_length=2, choices = HALL_NUMBER)
    side = models.CharField(max_length=10, choices = HALL_SIDE)
    machine_type = models.CharField(max_length=10, choices = TYPES_MAC)
    time_required = models.DurationField()
    time_start = models.DateTimeField(blank = True, null=True)
    availabilities = models.CharField(max_length=20, choices = AVAILABILITIES)
    def startLaundry(self):
        self.time_start = timezone.now()
        self.save()
    def __str__(self):
        return self.hall + self.side
    

class Queue_Entry(models.Model):
    machine = models.ForeignKey('laundry.Machine', related_name = 'user_queue', on_delete=models.CASCADE,)
    user = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(blank = True, null = True)
    
