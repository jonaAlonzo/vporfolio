# Generated by Django 4.1.5 on 2023-12-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0008_seguidor_alter_estudio_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seguido',
            options={'ordering': ['seguido'], 'verbose_name': 'Seguido', 'verbose_name_plural': 'seguidos'},
        ),
        migrations.RemoveField(
            model_name='seguido',
            name='seguid',
        ),
        migrations.AddField(
            model_name='seguido',
            name='seguido',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Seguido'),
        ),
    ]
