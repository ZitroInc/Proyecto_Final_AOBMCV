# Generated by Django 5.0 on 2023-12-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("monchis_log", "0002_comentario_delete_posteo_lista"),
    ]

    operations = [
        migrations.CreateModel(
            name="Posteo_Lista",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("subtitulo", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="post",
            name="imagen",
            field=models.ImageField(upload_to="media/foto_post/"),
        ),
    ]