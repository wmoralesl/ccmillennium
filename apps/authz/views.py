from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, authenticate
from django.shortcuts import redirect
from django.urls import reverse
from users.models import User
from django.contrib import messages

class LoginView(LoginView):
    template_name = 'auth/login.html'
    success_url = 'private:home'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirigir si el usuario ya está autenticado
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if not self.success_url:
            raise ValueError("No se ha configurado 'success_url'.")
        messages.success(self.request, 'Se ha iniciado sesión correctamente.')
        return reverse(self.success_url)
    
    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            messages.error(self.request, 'El usuario no existe')
            return super().form_invalid(form)
        
        if not user.is_active:
            messages.error(self.request, 'Su cuenta está desactivada. Comuniquese con un administrador')
        else:
            user_auth = authenticate(self.request, username=username, password=password )

            if user_auth is None:
                messages.error(self.request, 'La contraseña es incorrecta')
        return super().form_invalid(form)

        
def link_logout(request):
    logout(request)
    return redirect('public:home')