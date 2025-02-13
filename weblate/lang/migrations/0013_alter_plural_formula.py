# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.0.2 on 2022-02-18 13:37

from django.db import migrations, models

import weblate.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ("lang", "0012_alter_plural_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plural",
            name="formula",
            field=models.TextField(
                default="n != 1",
                validators=[weblate.utils.validators.validate_plural_formula],
                verbose_name="Plural formula",
            ),
        ),
    ]
