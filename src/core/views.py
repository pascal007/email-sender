from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from core.forms import SignUpForm


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        self.request.session.modified = True


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'sign-up.html'
    success_url = 'dashboard'

    def form_valid(self, form):
        form.save()
        email_addr = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(email=email_addr, password=raw_password)
        login(self.request, user)

        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        request.session.flush()
        return redirect('core:home-view')


