# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.3 on 2020-11-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Setting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.IntegerField(choices=[(1, "UI")], db_index=True)),
                ("name", models.CharField(max_length=100)),
                ("value", models.JSONField()),
            ],
            options={
                "unique_together": {("category", "name")},
            },
        ),
    ]
