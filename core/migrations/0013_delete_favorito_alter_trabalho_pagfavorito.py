# Generated by Django 5.0.6 on 2024-08-13 17:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_favorito_trabalho_pagfavorito"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Favorito",
        ),
        migrations.AlterField(
            model_name="trabalho",
            name="pagfavorito",
            field=models.ManyToManyField(blank=True, related_name="paginasfavoritos", to=settings.AUTH_USER_MODEL),
        ),
    ]