# Generated by Django 4.0.1 on 2022-02-11 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_fitness'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitness',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
            preserve_default=False,
        ),
    ]
