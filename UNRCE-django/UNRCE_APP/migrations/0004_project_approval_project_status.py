# Generated by Django 4.2.4 on 2023-09-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UNRCE_APP", "0003_sdg_description_alter_sdg_sdg"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="approval",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("accepted", "Accepted"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=8,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("submitted", "Submitted")],
                default="draft",
                max_length=20,
            ),
        ),
    ]