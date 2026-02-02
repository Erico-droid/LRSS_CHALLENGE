from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class LeaveRequest(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('normal', 'Normal Leave'),
        ('sick', 'Sick Leave'),
    ]
    
    user_firstname = models.CharField(
        max_length=30,
        null = False,
        blank = False,
    )
    user_lastname = models.CharField(
        max_length=30,
        null = False,
        blank = False,
    )
    start_date = models.DateField(
        null = False, 
        blank = False
    )
    end_date = models.DateField(
        null = False, 
        blank = False
    )
    leave_type = models.CharField(
        max_length=10, 
        choices=LEAVE_TYPE_CHOICES, 
        default='normal',
        null = False,
        blank = False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.user_firstname} {self.user_lastname} - {self.leave_type}"

    @property
    def number_of_days(self):
        """
            Calculate number of working days between start_date and end_date,
            DO NOT INCLUDE WEEKENDS (Saturday and Sunday)
        """
        if not self.start_date or not self.end_date:
            return 0

        day_count = 0
        current_day = self.start_date
        while current_day <= self.end_date:
            # monday - frifay is 0 to 4
            if current_day.weekday() < 5:
                day_count += 1
            current_day += timedelta(days=1)
        return day_count

    def save(self, *args, **kwargs):
        """
        My Thought Process... 
        If the end date falls on a weekend, adjust it to the next Monday. (Saturday -> +2 days, Sunday -> +1 day)
        """
        if self.end_date.weekday() == 5:  # If end date falls on Sat
            self.end_date += timedelta(days=2)
        elif self.end_date.weekday() == 6:  #If end date falls on Sun
            self.end_date += timedelta(days=1)
        super().save(*args, **kwargs)
