# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from django import forms
from django.utils.translation import gettext_lazy as _


class TOSForm(forms.Form):
    confirm = forms.BooleanField(
        label=_("I agree with the Terms of Service document"), required=True
    )
    next = forms.CharField(required=False, widget=forms.HiddenInput)
