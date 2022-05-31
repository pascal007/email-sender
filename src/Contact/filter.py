import django_filters
from DataAccessLayer.Contact.model import Contact
from DataAccessLayer.BaseModelFilter import BaseModelFilter


class ContactFilter(BaseModelFilter):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email')
