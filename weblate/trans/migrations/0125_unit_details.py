# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.7 on 2021-03-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0124_glossary_new_lang"),
    ]

    operations = [
        migrations.AddField(
            model_name="unit",
            name="details",
            field=models.JSONField(default=dict),
        ),
    ]
