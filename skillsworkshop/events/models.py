from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


# class Topic(models.Model):

#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


class Event(models.Model):
    # topic = models.ForeignKey(
    #     Topic,
    #     on_delete=models.CASCADE,
    #     related_name='events',

    # )
    topic = models.CharField(max_length=200)
    event_title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField()
    location = models.CharField(max_length=200)
    max_participants = models.CharField(max_length=200)  # should be integer
    image = models.URLField()
    is_open = models.BooleanField()
    sponser = models.CharField(max_length=100, blank=True)
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='organizer'
    )
    attendees = models.ManyToManyField(
        User,
        # on_delete=models.CASCADE,
        related_name='attendees',
        # blank=True,
    )

    def __str__(self):
        return self.event_title


@property
def max_capacity(self):
    # how to add max participants
    return self.max_participants.aggregate(sum=models.sum('max_participant'))['sum']
