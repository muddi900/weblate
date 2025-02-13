# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.5 on 2020-04-22 15:04

from django.db import migrations


def create_index(apps, schema_editor):
    if schema_editor.connection.vendor != "postgresql":
        return
    schema_editor.execute("DROP INDEX memory_source_fulltext")
    schema_editor.execute(
        "CREATE INDEX memory_source_trgm ON memory_memory USING GIN (source gin_trgm_ops)"
    )


def drop_index(apps, schema_editor):
    if schema_editor.connection.vendor != "postgresql":
        return
    schema_editor.execute("DROP INDEX memory_source_trgm")
    schema_editor.execute(
        "CREATE INDEX memory_source_fulltext ON memory_memory "
        "USING GIN (to_tsvector('english', source))"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("memory", "0006_memory_update"),
        ("trans", "0064_fulltext_index"),
    ]

    operations = [
        migrations.RunPython(create_index, drop_index, elidable=False, atomic=False)
    ]
