from django.db import models
from DataAccessLayer.BaseModel import BaseModel
from DataAccessLayer.constants import CONTACT_GROUP_CHOICES


class ContactGroup(BaseModel):
    title = models.CharField(
        max_length=255, null=True,
        blank=True, choices=CONTACT_GROUP_CHOICES,
        unique=True
    )

