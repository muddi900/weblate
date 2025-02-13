# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-08-03 08:42

from django.db import migrations, models

import weblate.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0093_auto_20200730_1432"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="language_aliases",
            field=models.CharField(
                default="",
                blank=True,
                help_text="Comma-separated list of language code mappings, for example: en_GB:en,en_US:en",
                max_length=200,
                validators=[weblate.utils.validators.validate_language_aliases],
                verbose_name="Language aliases",
            ),
        ),
    ]
