# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160208_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questions_text',
            new_name='question_text',
        ),
    ]
