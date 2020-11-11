# Usuário Costumizado Django - Português
Customização de usuário, autenticação, templates, Email como nome de usuário, para projectos Django

Código em inglês.<br>
Frontend em português.

<p><span style="color: red;">ATENÇÂO:</span> Definir no arquivo settings.py o 'Custom User model'</p>
<pre>AUTH_USER_MODEL = 'accounts.CustomUser'</pre>
<p>E no settings.py também, o app onde estiver o modelo de usuário costumizado, deve estar antes do 'django.contrib.admin',</p>
<pre>
# Application definition
INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
</pre>

<a href="https://ansistemas.com/custom_user_django/" target="_blank">Live Preview</a>

<img src="https://ansistemas.com/images/CustomUserDjango-FaceTwit.jpg" style="width:640px;height:auto;">
