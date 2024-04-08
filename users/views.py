import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    """Контроллер для регистрации нового пользователя"""

    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Отправка сообщения на почту"""
        new_user = form.save()
        # после регистрации is_active устанавливается в False (по дефолту он стоит в True)
        new_user.is_active = False
        # НЕ забыть сохранить изменения в модели
        new_user.save()
        url = reverse("users:activate_user", kwargs={"uid": new_user.activate_token})
        msg = f"для активации перейдите по ссылке: http://127.0.0.1:8000{url}"
        print(msg)
        send_mail(
            subject="Ку-ку!",
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user],
        )
        return super().form_valid(form)


def activate_user(request, uid):
    """Активация профиля по полученной ссылке"""
    model = User.objects.get(activate_token=uid)
    #  после подтверждения регистрации is_active выставляем в True
    model.is_active = True
    model.save()
    return redirect("users:congratulations")


def congratulations(request):
    """Контроллер для отправки поздравления с регистрацией"""
    return render(request, "users/congratulations.html")


class ProfileView(UpdateView):
    """Редактирование профиля"""

    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    """Генерация рандомного пароля"""
    new_password = [str(random.randint(0, 9)) for _ in range(6)]
    letters = [str(random.choice([chr(i) for i in range(97, 123)])) for _ in range(6)]
    new_password.extend(letters)
    random.shuffle(new_password)
    new_password = "".join(new_password)

    send_mail(
        subject="Смена пароля",
        message=f"Ваш новый пароль: {new_password}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse("catalog:home"))
