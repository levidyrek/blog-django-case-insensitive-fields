from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demonstration', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql=r'CREATE UNIQUE INDEX name_upper_idx ON demonstration_testmodel(UPPER(name));',
            reverse_sql=r'DROP INDEX name_upper_idx;'
        ),
        migrations.RunSQL(
            sql=r'CREATE UNIQUE INDEX email_upper_idx ON demonstration_testmodel(UPPER(email));',
            reverse_sql=r'DROP INDEX email_upper_idx;'
        ),
    ]
