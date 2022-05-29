from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView, FormView
from DataAccessLayer.Contact.model import Contact
from Contact.forms import AddContactForm, SendMailForm
from DataAccessLayer.ContactGroup.model import ContactGroup

from django.shortcuts import render, reverse


# Create your views here.


class ContactDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'contact_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(ContactDashboard, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.filter(
            created_by=self.request.user
        )

        return context


class AddContactView(LoginRequiredMixin, FormView):
    template_name = 'add_contact.html'
    form_class = AddContactForm

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        group = form.cleaned_data.get('group')

        try:
            group_type = ContactGroup.objects.get(title=group)

            Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                group=group_type,
                created_by=self.request.user
            )

        except ContactGroup.DoesNotExist:
            messages.error(self.request, "Group Category not yet configured")
            return reverse('contact:contact_dashboard')

        return super(AddContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse('contact:contact_dashboard')


class SendMailView(LoginRequiredMixin, View):
    template_name = 'send_mail.html'
    form = SendMailForm

    def get(self, request, id):
        recipient_contact = id
        try:
            recipient = Contact.objects.get(
                id=recipient_contact, created_by=self.request.user
            )
            context = {
                'recipient': recipient,
                'form': self.form
            }
            return render(self.request, self.template_name, context)

        except Contact.DoesNotExist:
            messages.error(self.request, 'Contact does not exist')
            return reverse('contact:contact_dashboard')

    def post(self, request, id):
        form = self.form(request.POST)

        try:
            contact = Contact.objects.get(
                id=id
            )
        except Contact.DoesNotExist:
            contact = None

        if contact and form.is_valid():
            subject = form.cleaned_data.get('subject')
            email = contact.email
            body = form.cleaned_data.get('body')

            messages.success(request, 'Mail sent successfully')
            return redirect('contact:contact_dashboard')

        else:
            messages.error(request, 'Mail could not be sent')

        return reverse('contact:contact_dashboard')



