# Generated by Django 4.1.5 on 2023-01-11 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("Name", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "department",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewEntery",
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
                ("name", models.CharField(max_length=100)),
                ("dob", models.DateField()),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                (
                    "purpose",
                    models.CharField(
                        choices=[
                            ("Enquiry", "Enquiry"),
                            ("Place_Order", "Place_Order"),
                            ("Return", "Return"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "materials",
                    models.CharField(
                        choices=[
                            ("NoteBook", "NoteBook"),
                            ("Exam_Paper", "Exam_Paper"),
                            ("Pen", "Pen"),
                            ("Drafter", "Drafter"),
                            ("Pencil", "Pencil"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.course",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.department",
                    ),
                ),
            ],
        ),
    ]
