# Generated by Django 4.2.4 on 2023-10-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UNRCE_APP', '0013_alter_project_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]