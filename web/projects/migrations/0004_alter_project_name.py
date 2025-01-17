# Generated by Django 4.2.3 on 2024-09-16 16:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_project_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="name",
            field=models.CharField(
                max_length=100,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Special characters (except dash) are not accepted",
                        regex="^[a-zA-Z0-9\\-]+$",
                    )
                ],
            ),
        ),
    ]
