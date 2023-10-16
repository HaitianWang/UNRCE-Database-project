# Generated by Django 4.2.4 on 2023-10-16 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UNRCE_APP', '0010_alter_project_audience'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='emails_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='org',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='rce_hub2',
            field=models.CharField(blank=True, choices=[('Great Southern', 'Great Southern'), ('Perth Metro', 'Perth Metro')], default='', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role_organisation',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]