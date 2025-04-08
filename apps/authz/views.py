from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse


class LoginView(LoginView):
    template_name = 'auth/login.html'
    success_url = 'private:home'

    def get_success_url(self):
        if not self.success_url:
            raise ValueError("No se ha configurado 'success_url'.")
        # messages.success(self.request, 'Se ha iniciado sesión correctamente.')
        return reverse(self.success_url)
        
def link_logout(request):
    logout(request)
    return redirect('public:home')