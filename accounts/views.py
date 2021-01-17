from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from accounts.models import CustomUser
from django.contrib.auth.views import (
	LoginView,
	PasswordChangeView,
	PasswordResetView,
	PasswordResetConfirmView,
	PasswordResetCompleteView,
	)


class UserLogin(SuccessMessageMixin, LoginView):
	template_name = 'accounts/login.html'


class UserCreate(SuccessMessageMixin, CreateView):
	model = CustomUser
	form_class = CustomUserCreateForm
	template_name = 'accounts/user-new.html'
	success_url = '/accounts/login'
	success_message = 'Bem vindo! Faça login para começar'


class UserChange(SuccessMessageMixin, UpdateView):
	model = CustomUser
	form_class = CustomUserChangeForm
	template_name = 'accounts/user-change.html'
	success_url = '/'
	success_message = 'O seu perfil foi alterado com sucesso'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)


class UserDelete(SuccessMessageMixin, DeleteView):
	model = CustomUser
	success_url = '/'
	template_name = 'accounts/user-delete.html'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
	template_name = 'accounts/password-change.html'
	success_url = '/'
	success_message = 'A sua senha foi alterada com sucesso'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
	template_name = 'accounts/password-reset.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
	success_message = 'A sua senha foi alterada corretamente. Faça login para começar'


class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
	template_name = 'accounts/password-reset-complete.html'
	success_message = 'A sua senha foi alterada corretamente. Faça login para começar'

	# For use with a html template, don't subscrive the 'get' method
	# and use the template 'template_name'
	def get(self, request, *args, **kwargs):

		return redirect('login')
