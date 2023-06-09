# Generated by Django 4.1.7 on 2023-03-31 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GenBankRecord",
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
                ("accession_id", models.CharField(max_length=100)),
                ("organism", models.CharField(max_length=100)),
                ("sequence_length", models.IntegerField()),
                ("molecule_type", models.CharField(max_length=50)),
                ("source", models.TextField()),
                ("taxonomy", models.TextField()),
                ("references", models.TextField()),
                ("sequence_data", models.TextField()),
            ],
        ),
    ]
