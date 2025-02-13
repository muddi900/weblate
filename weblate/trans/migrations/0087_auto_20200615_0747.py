# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-06-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0086_auto_20200609_1134"),
    ]

    operations = [
        migrations.AlterField(
            model_name="change",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterIndexTogether(
            name="change",
            index_together={("translation", "action", "timestamp")},
        ),
    ]
