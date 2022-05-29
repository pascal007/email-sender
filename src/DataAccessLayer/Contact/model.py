from django.db import models
from DataAccessLayer.BaseModel import BaseModel
from DataAccessLayer.ContactGroup.model import ContactGroup
from DataAccessLayer.User.model import User


class Contact(BaseModel):
    first_name = models.CharField(
        max_length=255, null=True, blank=True
    )
    last_name = models.CharField(
        max_length=255, null=True, blank=True
    )
    email = models.EmailField(
        max_length=255, null=True, blank=True
    )
    group = models.ForeignKey(
        ContactGroup,
        null=True, blank=True,
        related_name='contact_group',
        on_delete=models.SET_NULL
    )
    created_by = models.ForeignKey(
        User,
        null=True, blank=True, related_name='created_by',
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User,
        null=True, blank=True,
        related_name='updated_by',
        on_delete=models.CASCADE
    )
