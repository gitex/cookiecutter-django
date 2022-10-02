from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """ Default custom user model for {{cookiecutter.project_name}}. """

    # EMAIL_FIELD = 'email'
    # USERNAME_FIELD = EMAIL_FIELD
    # REQUIRED_FIELDS = []
    # username = None
    #
    # email = models.EmailField(
    #     verbose_name=_('Email'),
    #     unique=True,
    #     max_length=50,
    # )
    # first_name = models.CharField(
    #     max_length=50,
    #     verbose_name=_('First name'),
    # )
    # last_name = models.CharField(
    #     max_length=50,
    #     verbose_name=_('Last name'),
    # )
    # middle_name = models.CharField(
    #     max_length=50,
    #     verbose_name=_('Middle name'),
    #     default='',
    #     blank=True,
    # )

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
