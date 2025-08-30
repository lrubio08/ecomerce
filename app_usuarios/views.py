from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from app_usuarios.models import Usuarios
from .forms import UsuariosForm
from app_usuarios.utils import enviar_correo
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def registro(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password1'])
            usuario.save()

            # Usar la función enviar_correo
            subject = 'Bienvenido a nuestra plataforma'
            body = f"""
                <html>
                <body>
                <p> Hola <strong>{usuario.first_name} {usuario.last_name}</strong>,</p>
                <p>Gracias por registrarte. Puedes iniciar sesión aquí:</p>
                <p><a href=" http://127.0.0.1:8000/usuarios/login/ " style="color: #007BFF; text-decoration: none;">Iniciar sesión</a></p>
                </body>
                </html>
            """
            enviar_correo(subject, body, [usuario.email], is_html=True)

            return redirect(f"{reverse('registro')}?registro_exitoso=1")
    else:
        form = UsuariosForm()
    return render(request, 'app_usuarios/registro.html', {'form': form})

def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            messages.error(request, '¡Nombre de usuario o contraseña incorrectos!')
            return render(request, 'app_usuarios/login.html')
        return redirect('perfil_usuario')
    return render(request, 'app_usuarios/login.html')

def recuperar_password(request):
    return render(request, 'app_usuarios/recuperar_password.html')

def correo(request):
    return render(request, 'app_usuarios/correo.html')

@login_required
def perfil_usuario(request):
    usuario = request.user
    return render(request, 'app_usuarios/perfil_usuario.html', {'usuario': usuario})

@login_required
def actualizar_datos(request):
    usuario = request.user
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save() 
            return redirect('perfil_usuario')
        else:
            print("Errores del formulario:", form.errors)
    else:
        form = UsuariosForm(instance=usuario)    
    context = {
        'form': form,
        'usuario': usuario
    }
    return render(request, 'app_usuarios/actualizar_datos.html', context)
