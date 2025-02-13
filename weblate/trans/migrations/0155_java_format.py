# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1b1 on 2022-07-25 09:30

from django.db import migrations
from django.db.models import Q

from weblate.checks.flags import Flags


def fix_flags(text: str) -> str:
    flags = Flags(text)
    if "java-format" in flags:
        flags.remove("java-format")
        flags.merge("java-printf-format")
    if "java-messageformat" in flags:
        flags.remove("java-messageformat")
        flags.merge("java-format")
    return flags.format()


def fix_java_format(apps, schema_editor):
    Component = apps.get_model("trans", "Component")
    Unit = apps.get_model("trans", "Unit")

    updates = []
    for component in Component.objects.using(schema_editor.connection.alias).filter(
        Q(check_flags__contains="java-messageformat")
        | Q(check_flags__contains="java-format")
    ):
        fixed = fix_flags(component.check_flags)
        if fixed != component.check_flags:
            component.check_flags = fixed
            updates.append(component)

    Component.objects.using(schema_editor.connection.alias).bulk_update(
        updates, ["check_flags"]
    )

    updates = []
    for unit in Unit.objects.using(schema_editor.connection.alias).filter(
        Q(extra_flags__contains="java-messageformat")
        | Q(extra_flags__contains="java-format")
    ):
        fixed = fix_flags(unit.extra_flags)
        if fixed != unit.extra_flags:
            unit.extra_flags = fixed
            updates.append(unit)

    Unit.objects.using(schema_editor.connection.alias).bulk_update(
        updates, ["extra_flags"]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0154_alter_component_language_code_style"),
    ]

    operations = [migrations.RunPython(fix_java_format, elidable=True)]
