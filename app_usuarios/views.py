from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from app_usuarios.models import Usuarios
from .forms import UsuariosForm, RecuperarPasswordForm
from app_usuarios.utils import enviar_correo
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


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

def correo_recuperacion_password(request):
    if request.method == 'POST':
        form = RecuperarPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                usuario = Usuarios.objects.get(email=email)
            except Usuarios.DoesNotExist:
                form.add_error('email', 'Este correo no está registrado.')
                return render(request, 'app_usuarios/correo_recuperacion_password.html', {'form': form})

            # Generar token y enlace seguro
            token = default_token_generator.make_token(usuario)
            uid = urlsafe_base64_encode(force_bytes(usuario.pk))
            link = request.build_absolute_uri(
                reverse('recuperar_password', kwargs={'uidb64': uid, 'token': token})
            )

            # Enviar correo
            subject = 'Recupera tu contraseña'
            body = f"""
                <html>
                <body>
                <p>Hola <strong>{usuario.first_name} {usuario.last_name}</strong>,</p>
                <p>Haz clic en el siguiente enlace para establecer una nueva contraseña:</p>
                <p><a href="{link}" style="color: #007BFF; text-decoration: none;">Recuperar contraseña</a></p>
                </body>
                </html>
            """
            enviar_correo(subject, body, [usuario.email], is_html=True)

            return redirect(f"{reverse('correo_recuperacion_password')}?correo_recuperacion_exitosa=1")
    else:
        form = RecuperarPasswordForm()
    return render(request, 'app_usuarios/correo_recuperacion_password.html', {'form': form})


def recuperar_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        usuario = Usuarios.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Usuarios.DoesNotExist):
        usuario = None

    if usuario is not None and default_token_generator.check_token(usuario, token):
        if request.method == 'POST':
            nueva_password = request.POST.get('password')
            usuario.set_password(nueva_password)
            usuario.save()
            return redirect('login')
        return render(request, 'app_usuarios/recuperar_password.html', {'usuario': usuario})
    else:
        return render(request, 'app_usuarios/correo_recuperacion_password.html', {
            'error': 'El enlace ha expirado o es inválido. Por favor solicita uno nuevo.'
        })


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
